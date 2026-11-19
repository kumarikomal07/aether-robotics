/* Aether Robotics — site interactions & motion */
(function () {
  "use strict";

  /* ------------------------------------------------------------
     CONFIGURATION — fill these in before going live
     ------------------------------------------------------------ */
  var CONFIG = {
    // Google Analytics 4 ID, e.g. "G-XXXXXXXXXX". Loads only after analytics consent.
    gaId: "",
    // POST endpoints (e.g. Formspree "https://formspree.io/f/xxxx"). Empty = demo mode:
    // forms validate and show a success message but send nothing.
    enquiryEndpoint: "",
    careersEndpoint: "",
    newsletterEndpoint: ""
  };
  var SITE = window.AE_SITE || {};
  var CONSENT_KEY = "ae_consent";

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var root = document.documentElement;

  /* ---------- loader ---------- */
  function loaded() { root.classList.add("loaded"); }
  if (document.readyState === "complete") loaded(); else window.addEventListener("load", loaded);
  setTimeout(loaded, 2200); // never block content for long

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- header, progress, back to top ---------- */
  var header = $("[data-header]"), progress = $(".progress"), toTop = $(".to-top"), lastY = 0;
  function onScroll() {
    var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight, p = h > 0 ? (y / h).toFixed(4) : 0;
    if (progress) progress.style.setProperty("--p", p);
    if (toTop) { toTop.style.setProperty("--p", p); toTop.classList.toggle("show", y > 700); }
    if (header) {
      header.classList.toggle("scrolled", y > 20);
      header.classList.toggle("hide", y > lastY && y > 600 && !document.body.classList.contains("nav-open"));
    }
    lastY = y;
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* ---------- navigation ---------- */
  var toggle = $(".nav-toggle");
  function setNav(open) {
    document.body.classList.toggle("nav-open", open);
    if (toggle) { toggle.setAttribute("aria-expanded", String(open)); toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu"); }
  }
  if (toggle) toggle.addEventListener("click", function () { setNav(!document.body.classList.contains("nav-open")); });
  document.addEventListener("click", function (e) {
    if (document.body.classList.contains("nav-open") && !e.target.closest(".nav") && !e.target.closest(".nav-toggle")) setNav(false);
    if (!e.target.closest(".has-dd")) closeDds();
  });
  function closeDds(except) {
    $$(".has-dd.open").forEach(function (x) { if (x !== except) { x.classList.remove("open"); $(".dd-btn", x).setAttribute("aria-expanded", "false"); } });
  }
  $$(".dd-btn").forEach(function (b) {
    b.addEventListener("click", function (e) {
      e.stopPropagation();
      var li = b.parentElement, open = !li.classList.contains("open");
      closeDds(li);
      li.classList.toggle("open", open);
      b.setAttribute("aria-expanded", String(open));
    });
  });
  $$(".nav a").forEach(function (a) { a.addEventListener("click", function () { setNav(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") { setNav(false); closeDds(); } });

  /* ---------- split headings into words ---------- */
  function splitEl(el) {
    var i = 0, frag = document.createDocumentFragment();
    function word(txt, cls) {
      var w = document.createElement("span"); w.className = "w";
      var s = document.createElement("span"); s.textContent = txt; s.style.setProperty("--i", i++);
      if (cls) s.className = cls;
      w.appendChild(s); return w;
    }
    function walk(nodes, cls) {
      nodes.forEach(function (n) {
        if (n.nodeType === 3) {
          n.textContent.split(/(\s+)/).forEach(function (p) {
            if (!p) return;
            frag.appendChild(/^\s+$/.test(p) ? document.createTextNode(" ") : word(p, cls));
          });
        } else if (n.nodeName === "BR") frag.appendChild(n.cloneNode());
        else walk(Array.prototype.slice.call(n.childNodes), n.className || cls);
      });
    }
    walk(Array.prototype.slice.call(el.childNodes), "");
    el.setAttribute("aria-label", el.textContent.replace(/\s+/g, " ").trim());
    el.textContent = "";
    el.appendChild(frag);
    $$(".w", el).forEach(function (w) { w.setAttribute("aria-hidden", "true"); });
    el.classList.add("split");
  }
  if (!reduce) $$("[data-split]").forEach(splitEl);

  /* ---------- reveal on scroll ---------- */
  var revealTargets = $$("[data-reveal], .split, [data-process], .cap");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("in");
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.1 });
    revealTargets.forEach(function (el) { io.observe(el); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- counters ---------- */
  if ("IntersectionObserver" in window && !reduce) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        co.unobserve(en.target);
        var el = en.target, end = +el.getAttribute("data-count"), t0 = null;
        el.textContent = "0";
        (function step(t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / 1600, 1);
          el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
          if (p < 1) requestAnimationFrame(step);
        })(performance.now());
      });
    }, { threshold: 0.6 });
    $$("[data-count]").forEach(function (c) { co.observe(c); });
  }

  /* ---------- typing status line ---------- */
  $$("[data-typer]").forEach(function (el) {
    if (reduce) return;
    var words = el.getAttribute("data-typer").split("|"), wi = 0, ci = words[0].length, del = true;
    function tick() {
      var w = words[wi];
      if (del) { ci--; if (ci <= 0) { del = false; wi = (wi + 1) % words.length; } }
      else { ci++; if (ci >= words[wi].length) { del = true; el.textContent = words[wi]; return setTimeout(tick, 2600); } }
      el.textContent = words[wi].slice(0, Math.max(ci, 0)) || " ";
      setTimeout(tick, del ? 40 : 75);
    }
    setTimeout(tick, 3200);
  });

  /* ---------- parallax ---------- */
  var para = $$("[data-parallax]");
  if (para.length && !reduce) {
    var ticking = false;
    var runPara = function () {
      var vh = window.innerHeight;
      para.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var off = (r.top + r.height / 2 - vh / 2) * -(parseFloat(el.getAttribute("data-parallax")) || 0.1);
        el.style.transform = "translate3d(0," + off.toFixed(1) + "px,0)";
      });
      ticking = false;
    };
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(runPara); } }, { passive: true });
    runPara();
  }

  /* ---------- pointer effects ---------- */
  if (finePointer && !reduce) {
    var glow = $(".cursor-glow");
    document.addEventListener("mousemove", function (e) {
      if (glow) { glow.style.setProperty("--cx", e.clientX + "px"); glow.style.setProperty("--cy", e.clientY + "px"); }
      var g = e.target.closest && e.target.closest("[data-glow]");
      if (!g) return;
      var r = g.getBoundingClientRect();
      g.style.setProperty("--mx", (e.clientX - r.left) + "px");
      g.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
    $$(".btn-primary").forEach(function (b) {
      b.addEventListener("mousemove", function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = "translate(" + ((e.clientX - r.left - r.width / 2) * 0.15).toFixed(1) + "px," + ((e.clientY - r.top - r.height / 2) * 0.25 - 2).toFixed(1) + "px)";
      });
      b.addEventListener("mouseleave", function () { b.style.transform = ""; });
    });
    $$("[data-tilt]").forEach(function (el) {
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = "perspective(1000px) rotateY(" + (x * 7).toFixed(2) + "deg) rotateX(" + (-y * 7).toFixed(2) + "deg)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    });
    var scene = $("[data-scene]"), hero = $("[data-hero]");
    if (scene && hero) {
      var tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
      var loop = function () {
        cx += (tx - cx) * 0.06; cy += (ty - cy) * 0.06;
        scene.style.setProperty("--px", cx.toFixed(3)); scene.style.setProperty("--py", cy.toFixed(3));
        raf = (Math.abs(tx - cx) > 0.002 || Math.abs(ty - cy) > 0.002) ? requestAnimationFrame(loop) : null;
      };
      hero.addEventListener("mousemove", function (e) {
        tx = (e.clientX / window.innerWidth - 0.5) * 2; ty = (e.clientY / window.innerHeight - 0.5) * 2;
        if (!raf) raf = requestAnimationFrame(loop);
      });
    }
  }

  /* ---------- particle network canvases ---------- */
  function Net(canvas) {
    var ctx = canvas.getContext("2d"), pts = [], w = 0, h = 0, dpr = Math.min(window.devicePixelRatio || 1, 2), running = false, mouse = null, host = canvas.parentElement;
    function size() {
      var r = host.getBoundingClientRect();
      w = r.width; h = r.height; canvas.width = w * dpr; canvas.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.min(80, Math.round((w * h) / 18000)); pts = [];
      for (var i = 0; i < n; i++) pts.push({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - .5) * .3, vy: (Math.random() - .5) * .3, r: Math.random() * 1.5 + .5 });
    }
    function draw() {
      ctx.clearRect(0, 0, w, h);
      var max = 120;
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        if (running) { p.x += p.vx; p.y += p.vy; if (p.x < 0 || p.x > w) p.vx *= -1; if (p.y < 0 || p.y > h) p.vy *= -1; }
        for (var j = i + 1; j < pts.length; j++) {
          var q = pts[j], dx = p.x - q.x, dy = p.y - q.y, d = dx * dx + dy * dy;
          if (d < max * max) { ctx.strokeStyle = "rgba(94,235,255," + (0.16 * (1 - Math.sqrt(d) / max)).toFixed(3) + ")"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y); ctx.stroke(); }
        }
        if (mouse) {
          var mx = p.x - mouse.x, my = p.y - mouse.y, md = mx * mx + my * my;
          if (md < 170 * 170) { ctx.strokeStyle = "rgba(34,211,238," + (0.45 * (1 - Math.sqrt(md) / 170)).toFixed(3) + ")"; ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke(); }
        }
        ctx.fillStyle = "rgba(170,240,255,.8)"; ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.283); ctx.fill();
      }
      if (running) requestAnimationFrame(draw);
    }
    size(); draw();
    if (reduce) return;
    if (finePointer) {
      host.addEventListener("mousemove", function (e) { var r = canvas.getBoundingClientRect(); mouse = { x: e.clientX - r.left, y: e.clientY - r.top }; });
      host.addEventListener("mouseleave", function () { mouse = null; });
    }
    new IntersectionObserver(function (en) {
      var vis = en[0].isIntersecting;
      if (vis && !running) { running = true; requestAnimationFrame(draw); } else if (!vis) running = false;
    }).observe(canvas);
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { size(); if (!running) draw(); }, 200); });
  }
  if ("IntersectionObserver" in window) $$("canvas.net").forEach(Net);

  /* ---------- product tabs (autoplay) ---------- */
  $$("[data-tabs]").forEach(function (box) {
    var tabs = $$("[data-tab]", box), panes = $$(".pt-pane", box), cur = 0, timer = null;
    var dur = +box.getAttribute("data-autoplay") || 0;
    box.style.setProperty("--dur", dur / 1000 + "s");
    function show(i, focus) {
      cur = i;
      tabs.forEach(function (t, k) { var on = k === i; t.classList.toggle("on", on); t.setAttribute("aria-selected", String(on)); t.tabIndex = on ? 0 : -1; });
      panes.forEach(function (p, k) { var on = k === i; p.classList.toggle("on", on); p.hidden = !on; });
      if (focus) tabs[i].focus();
      // restart bar animation
      var bar = $(".bar", tabs[i]); if (bar) { bar.style.animation = "none"; void bar.offsetWidth; bar.style.animation = ""; }
      schedule();
    }
    function schedule() { clearTimeout(timer); if (dur && !reduce && !box.classList.contains("paused")) timer = setTimeout(function () { show((cur + 1) % tabs.length); }, dur); }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { show(i); });
      t.addEventListener("keydown", function (e) {
        var k = e.key === "ArrowRight" || e.key === "ArrowDown" ? 1 : e.key === "ArrowLeft" || e.key === "ArrowUp" ? -1 : 0;
        if (k) { e.preventDefault(); show((i + k + tabs.length) % tabs.length, true); }
      });
    });
    box.addEventListener("mouseenter", function () { box.classList.add("paused"); clearTimeout(timer); });
    box.addEventListener("mouseleave", function () { box.classList.remove("paused"); schedule(); });
    box.addEventListener("focusin", function () { box.classList.add("paused"); clearTimeout(timer); });
    if ("IntersectionObserver" in window) new IntersectionObserver(function (en) { if (en[0].isIntersecting) schedule(); else clearTimeout(timer); }).observe(box);
    show(0);
  });

  /* ---------- industry expanding panels ---------- */
  $$("[data-panels]").forEach(function (wrap) {
    var ps = $$(".ind-panel", wrap);
    ps.forEach(function (p) {
      function act() { ps.forEach(function (x) { x.classList.toggle("on", x === p); }); }
      p.addEventListener("mouseenter", act);
      p.addEventListener("focus", act);
      p.addEventListener("click", function (e) { if (!p.classList.contains("on")) { e.preventDefault(); act(); } });
    });
  });

  /* ---------- filters ---------- */
  $$("[data-filters]").forEach(function (group) {
    var name = group.getAttribute("data-filters"), grid = $('[data-filter-grid="' + name + '"]'), empty = $('[data-empty="' + name + '"]');
    if (!grid) return;
    group.addEventListener("click", function (e) {
      var b = e.target.closest("[data-filter]");
      if (!b) return;
      var f = b.getAttribute("data-filter"), shown = 0;
      $$("[data-filter]", group).forEach(function (x) { var on = x === b; x.classList.toggle("on", on); x.setAttribute("aria-pressed", String(on)); });
      Array.prototype.slice.call(grid.children).forEach(function (c) {
        var match = f === "all" || c.getAttribute("data-cat") === f;
        c.classList.toggle("out", !match);
        if (match) { shown++; c.classList.add("in"); }
      });
      if (empty) empty.hidden = shown > 0;
      grid.parentElement.classList.remove("is-filtering"); void grid.offsetWidth; grid.parentElement.classList.add("is-filtering");
    });
  });

  /* ---------- sub-nav scrollspy ---------- */
  var spyLinks = $$("[data-spy]");
  if (spyLinks.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        spyLinks.forEach(function (a) {
          var on = a.getAttribute("data-spy") === en.target.id;
          a.classList.toggle("on", on);
          if (on) a.parentElement.scrollTo({ left: a.offsetLeft - 16, behavior: "smooth" });
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    spyLinks.forEach(function (a) { var t = document.getElementById(a.getAttribute("data-spy")); if (t) spy.observe(t); });
  }

  /* ---------- WhatsApp (hidden until a number is configured), copy, social ---------- */
  if (SITE.whatsapp) {
    $$("[data-wa]").forEach(function (a) {
      a.href = "https://wa.me/" + SITE.whatsapp + "?text=" + encodeURIComponent("Hello Aether Robotics, I'd like to discuss a project.");
      a.target = "_blank"; a.rel = "noopener"; a.hidden = false;
    });
  } else {
    document.body.classList.add("no-wa");
  }
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var u = b.getAttribute("data-copy");
      (navigator.clipboard ? navigator.clipboard.writeText(u) : Promise.reject()).then(function () {
        b.setAttribute("aria-label", "Link copied"); b.style.background = "var(--cyan)"; b.style.color = "#00121C";
        setTimeout(function () { b.setAttribute("aria-label", "Copy link"); b.style.background = ""; b.style.color = ""; }, 1600);
      }).catch(function () { window.prompt("Copy this link:", u); });
    });
  });
  $$("[data-social]").forEach(function (a) { a.title = "Social profile link coming soon"; a.addEventListener("click", function (e) { e.preventDefault(); }); });

  /* ---------- forms ---------- */
  var EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function setErr(field, msg) {
    var wrap = field.closest(".field") || field.closest(".check");
    if (!wrap) return;
    var old = $(".f-err", wrap); if (old) old.remove();
    wrap.classList.toggle("err", !!msg);
    field.setAttribute("aria-invalid", msg ? "true" : "false");
    if (msg && wrap.classList.contains("field")) {
      var p = document.createElement("span"); p.className = "f-err"; p.id = (field.id || field.name) + "-err"; p.textContent = msg;
      wrap.appendChild(p); field.setAttribute("aria-describedby", p.id);
    }
  }
  function check(f) {
    if (f.type === "hidden" || f.classList.contains("hp") || f.disabled) return "";
    var v = (f.value || "").trim();
    if (f.type === "checkbox") return f.required && !f.checked ? "Please confirm to continue." : "";
    if (f.type === "file") {
      if (f.required && !f.files.length) return "Please upload your CV.";
      if (f.files.length) {
        var file = f.files[0], max = (+f.getAttribute("data-max") || 5) * 1048576;
        if (!/\.(pdf|docx?)$/i.test(file.name)) return "Please upload a PDF, DOC or DOCX file.";
        if (file.size > max) return "File is larger than " + (max / 1048576) + " MB.";
      }
      return "";
    }
    if (f.required && !v) return "This field is required.";
    if (v && f.type === "email" && !EMAIL.test(v)) return "Please enter a valid email address.";
    if (v && f.type === "url" && !/^https?:\/\/\S+\.\S+/.test(v)) return "Please enter a full URL starting with https://";
    if (v && f.type === "tel" && !/^[+()\d\s-]{7,20}$/.test(v)) return "Please enter a valid phone number.";
    if (v && f.minLength > 0 && v.length < f.minLength) return "Please add a little more detail (at least " + f.minLength + " characters).";
    return "";
  }
  function send(endpoint, form) {
    if (!endpoint) return new Promise(function (res) { setTimeout(res, 900); });
    return fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); });
  }
  $$("form[data-form]").forEach(function (form) {
    var kind = form.getAttribute("data-form"), fields = $$("input, select, textarea", form), msg = $(".form-msg", form);
    fields.forEach(function (f) {
      f.addEventListener("blur", function () { if (f.type !== "file") setErr(f, check(f)); });
      f.addEventListener("input", function () { if (f.closest(".err")) setErr(f, check(f)); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if ($(".hp", form).value) return;
      var first = null;
      fields.forEach(function (f) { var m = check(f); setErr(f, m); if (m && !first) first = f; });
      if (first) { msg.className = "form-msg bad"; msg.textContent = "Please correct the highlighted fields."; first.focus(); return; }
      var btn = $("button[type=submit]", form);
      btn.classList.add("loading"); msg.className = "form-msg"; msg.textContent = "Sending…";
      send(kind === "careers" ? CONFIG.careersEndpoint : CONFIG.enquiryEndpoint, form).then(function () {
        msg.className = "form-msg ok";
        msg.textContent = kind === "careers" ? "Thank you. Your application has been received and we will be in touch if there is a suitable match." : "Thank you. Your enquiry has been received and an engineer will reply within one business day.";
        form.reset(); resetFile(form);
      }).catch(function () {
        msg.className = "form-msg bad"; msg.textContent = "Sorry, something went wrong. Please email us directly.";
      }).then(function () { btn.classList.remove("loading"); });
    });
  });
  function resetFile(form) { $$(".file", form).forEach(function (l) { l.classList.remove("has"); var s = $("[data-file-label]", l); if (s) s.textContent = "Click to upload or drag your file here"; }); }
  $$(".file").forEach(function (label) {
    var input = $("input[type=file]", label), txt = $("[data-file-label]", label);
    input.addEventListener("change", function () {
      var f = input.files[0];
      label.classList.toggle("has", !!f);
      txt.textContent = f ? f.name + " (" + (f.size / 1048576).toFixed(2) + " MB)" : "Click to upload or drag your file here";
      setErr(input, check(input));
    });
    ["dragenter", "dragover"].forEach(function (ev) { label.addEventListener(ev, function (e) { e.preventDefault(); label.classList.add("drag"); }); });
    ["dragleave", "drop"].forEach(function (ev) { label.addEventListener(ev, function (e) { e.preventDefault(); label.classList.remove("drag"); }); });
    label.addEventListener("drop", function (e) { if (e.dataTransfer.files.length) { input.files = e.dataTransfer.files; input.dispatchEvent(new Event("change")); } });
  });

  // prefill the enquiry form from the URL (?interest=robotics, ?type=project|partnership, ?industry=logistics)
  var qs = new URLSearchParams(location.search), sel = $("#e-service"), msgBox = $("#e-msg"), typeIn = $('input[name="type"]');
  if (sel) {
    var it = qs.get("interest"), t = qs.get("type"), ind = qs.get("industry");
    if (it && $('option[value="' + it + '"]', sel)) sel.value = it;
    if (t === "partnership") sel.value = "partnership";
    if (typeIn && t) typeIn.value = t;
    if (ind && msgBox && !msgBox.value) msgBox.value = "Industry: " + ind.replace(/-/g, " ") + "\n\n";
  }
  $$("[data-area]").forEach(function (a) { a.addEventListener("click", function () { var s = $("#c-area"); if (s) s.value = a.getAttribute("data-area"); }); });

  // newsletter
  $$("form[data-newsletter]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = $("input[type=email]", form), msg = $(".form-msg", form);
      if ($(".hp", form).value) return;
      if (!EMAIL.test(input.value.trim())) { msg.className = "form-msg bad"; msg.textContent = "Please enter a valid email address."; input.focus(); return; }
      send(CONFIG.newsletterEndpoint, form).then(function () {
        msg.className = "form-msg ok"; msg.textContent = "Thanks for subscribing!"; form.reset();
      }).catch(function () { msg.className = "form-msg bad"; msg.textContent = "Sorry, please try again later."; });
    });
  });

  /* ---------- cookie consent ---------- */
  function getConsent() { try { return JSON.parse(localStorage.getItem(CONSENT_KEY) || "null"); } catch (e) { return null; } }
  function saveConsent(c) {
    c.ts = Date.now();
    try { localStorage.setItem(CONSENT_KEY, JSON.stringify(c)); } catch (e) { /* storage blocked */ }
    applyConsent(c);
  }
  function applyConsent(c) {
    if (c && c.analytics && CONFIG.gaId && !window.gtag) {
      var s = document.createElement("script"); s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + CONFIG.gaId; document.head.appendChild(s);
      window.dataLayer = window.dataLayer || []; window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date()); window.gtag("config", CONFIG.gaId, { anonymize_ip: true });
    }
  }
  var banner = $("[data-cookie]"), consent = getConsent(), prefs = $("[data-prefs]");
  if (consent && Date.now() - consent.ts > 365 * 864e5) consent = null;
  if (!consent && banner && !prefs) setTimeout(function () { banner.hidden = false; }, 1800);
  applyConsent(consent);
  function syncPrefs(c) { if (!prefs) return; $('[name="analytics"]', prefs).checked = !!(c && c.analytics); $('[name="marketing"]', prefs).checked = !!(c && c.marketing); }
  syncPrefs(consent);
  function prefMsg(t) { if (prefs) { var m = $(".form-msg", prefs); m.className = "form-msg ok"; m.textContent = t; } }
  $$("[data-consent]").forEach(function (b) {
    b.addEventListener("click", function () {
      var all = b.getAttribute("data-consent") === "accept", c = { analytics: all, marketing: all };
      saveConsent(c); syncPrefs(c);
      if (banner) banner.hidden = true;
      prefMsg(all ? "All cookies accepted." : "Optional cookies rejected.");
    });
  });
  if (prefs) prefs.addEventListener("submit", function (e) {
    e.preventDefault();
    saveConsent({ analytics: $('[name="analytics"]', prefs).checked, marketing: $('[name="marketing"]', prefs).checked });
    prefMsg("Your preferences have been saved.");
  });
})();
