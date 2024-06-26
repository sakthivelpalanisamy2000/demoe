!(function (e) {
  var t = {};
  function o(n) {
    if (t[n]) return t[n].exports;
    var r = (t[n] = { i: n, l: !1, exports: {} });
    return e[n].call(r.exports, r, r.exports, o), (r.l = !0), r.exports;
  }
  (o.m = e),
    (o.c = t),
    (o.d = function (e, t, n) {
      o.o(e, t) || Object.defineProperty(e, t, { enumerable: !0, get: n });
    }),
    (o.r = function (e) {
      "undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 });
    }),
    (o.t = function (e, t) {
      if ((1 & t && (e = o(e)), 8 & t)) return e;
      if (4 & t && "object" == typeof e && e && e.__esModule) return e;
      var n = Object.create(null);
      if (
        (o.r(n),
        Object.defineProperty(n, "default", { enumerable: !0, value: e }),
        2 & t && "string" != typeof e)
      )
        for (var r in e)
          o.d(
            n,
            r,
            function (t) {
              return e[t];
            }.bind(null, r)
          );
      return n;
    }),
    (o.n = function (e) {
      var t =
        e && e.__esModule
          ? function () {
              return e.default;
            }
          : function () {
              return e;
            };
      return o.d(t, "a", t), t;
    }),
    (o.o = function (e, t) {
      return Object.prototype.hasOwnProperty.call(e, t);
    }),
    (o.p = "/public/build"),
    o((o.s = 2));
})([
  function (e, t) {
    const o = {
        C: "c",
        CPP: "cpp",
        PYTHON: "python",
        JAVA: "java",
        JAVASCRIPT: "javascript",
        CSHARP: "csharp",
        GOLANG: "golang",
        RUST: "rust",
        R: "r",
        PHP: "php",
        SWIFT: "swift",
      },
      n = o.PYTHON,
      r = {
        [o.C]: "c_cpp",
        [o.CPP]: "c_cpp",
        [o.PYTHON]: "python",
        [o.JAVA]: "java",
        [o.JAVASCRIPT]: "javascript",
        [o.CSHARP]: "csharp",
        [o.GOLANG]: "golang",
        [o.RUST]: "rust",
        [o.R]: "r",
        [o.PHP]: "php",
        [o.SWIFT]: "swift",
      };
    e.exports = {
      DEFAULT_SHELL: "dash",
      SUPPORTED_LANGUAGES: o,
      DEFAULT_LANGUAGE: n,
      ACE_EDITOR_MODES: r,
    };
  },
  function (e, t, o) {
    e.exports = (function () {
      "use strict";
      function e(e) {
        for (var t = 1; t < arguments.length; t++) {
          var o = arguments[t];
          for (var n in o) e[n] = o[n];
        }
        return e;
      }
      return (function t(o, n) {
        function r(t, r, a) {
          if ("undefined" != typeof document) {
            "number" == typeof (a = e({}, n, a)).expires &&
              (a.expires = new Date(Date.now() + 864e5 * a.expires)),
              a.expires && (a.expires = a.expires.toUTCString()),
              (t = encodeURIComponent(t)
                .replace(/%(2[346B]|5E|60|7C)/g, decodeURIComponent)
                .replace(/[()]/g, escape));
            var i = "";
            for (var s in a)
              a[s] &&
                ((i += "; " + s),
                !0 !== a[s] && (i += "=" + a[s].split(";")[0]));
            return (document.cookie = t + "=" + o.write(r, t) + i);
          }
        }
        return Object.create(
          {
            set: r,
            get: function (e) {
              if ("undefined" != typeof document && (!arguments.length || e)) {
                for (
                  var t = document.cookie ? document.cookie.split("; ") : [],
                    n = {},
                    r = 0;
                  r < t.length;
                  r++
                ) {
                  var a = t[r].split("="),
                    i = a.slice(1).join("=");
                  try {
                    var s = decodeURIComponent(a[0]);
                    if (((n[s] = o.read(i, s)), e === s)) break;
                  } catch (e) {}
                }
                return e ? n[e] : n;
              }
            },
            remove: function (t, o) {
              r(t, "", e({}, o, { expires: -1 }));
            },
            withAttributes: function (o) {
              return t(this.converter, e({}, this.attributes, o));
            },
            withConverter: function (o) {
              return t(e({}, this.converter, o), this.attributes);
            },
          },
          {
            attributes: { value: Object.freeze(n) },
            converter: { value: Object.freeze(o) },
          }
        );
      })(
        {
          read: function (e) {
            return (
              '"' === e[0] && (e = e.slice(1, -1)),
              e.replace(/(%[\dA-F]{2})+/gi, decodeURIComponent)
            );
          },
          write: function (e) {
            return encodeURIComponent(e).replace(
              /%(2[346BF]|3[AC-F]|40|5[BDE]|60|7[BCD])/g,
              decodeURIComponent
            );
          },
        },
        { path: "/" }
      );
    })();
  },
  function (e, t, o) {
    "use strict";
    o.r(t);
    const n = "mobile--tabbed-compiler",
      r = "mobile--tabbed--terminal",
      a =
        '<span class="run-text">\n                                &nbsp;Run&nbsp;\n                              </span>\n';
    var i = o(0);
    const s = () => {
      const e = (() => {
          const e = "https://programiz.pro";
          let t = "";
          return (
            lang === i.SUPPORTED_LANGUAGES.C
              ? (t = e + "/learn/master-c-programming")
              : lang === i.SUPPORTED_LANGUAGES.PYTHON
              ? (t = e + "/learn/master-python")
              : lang === i.SUPPORTED_LANGUAGES.JAVA
              ? (t = e + "/learn/master-java")
              : lang === i.SUPPORTED_LANGUAGES.CPP &&
                (t = e + "/learn/master-cpp"),
            (t +=
              "?utm_source=compiler-output-popup&utm_campaign=programiz&utm_medium=referral"),
            t
          );
        })(),
        t = $("#root").data("lang"),
        o =
          (function (e) {
            let t = "Coding";
            switch (e) {
              case i.SUPPORTED_LANGUAGES.C:
                t = "C";
                break;
              case i.SUPPORTED_LANGUAGES.CPP:
                t = "C++";
                break;
              case i.SUPPORTED_LANGUAGES.JAVA:
                t = "Java";
                break;
              case i.SUPPORTED_LANGUAGES.PYTHON:
                t = "Python";
                break;
              case i.SUPPORTED_LANGUAGES.SQL:
                t = "SQL";
            }
            return t;
          })(t) + " Course, Enhanced by AI",
        n = `Learn ${t} the right way — solve challenges, build projects, and leverage the power of AI to aid you in handling errors.`;
      $(".sale-popup #discount-description").html(o),
        $(".sale-popup .sale-container h5").html(n),
        $(".sale-popup > a")
          .html("Get Started for Free")
          .attr("title", "Get Started for Free")
          .attr("href", e),
        (document.getElementById("sale-popup").style.display = "flex");
    };
    function l() {
      const e = new Date("Nov 27, 2023 13:45:00 GMT+0545").getTime(),
        t = new Date("Nov 28, 2023 13:45:00 GMT+0545").getTime(),
        o = new Date().getTime();
      return o >= e && o < t;
    }
    function c() {
      l() &&
        (!(function (e) {
          o();
          const t = setInterval(o, 1e3);
          function o() {
            let o = new Date().getTime();
            const n = e - o;
            let r = Math.floor(n / 864e5),
              a = Math.floor((n % 864e5) / 36e5),
              i = Math.floor((n % 36e5) / 6e4),
              s = Math.floor((n % 6e4) / 1e3);
            o > e && ((r = 0), (a = 0), (i = 0), (s = 0), clearInterval(t)),
              r < 10 && (r = "0" + r),
              a < 10 && (a = "0" + a),
              i < 10 && (i = "0" + i),
              s < 10 && (s = "0" + s),
              $("#sale-time-countdown").html(
                r + "d : " + a + "hrs : " + i + "mins : " + s + "s"
              );
          }
        })(new Date("Nov 28, 2023 13:45:00 GMT+0545").getTime()),
        $("#sale-top-banner").removeClass("d-none"));
    }
    function p() {
      const e = new Date("Nov 28, 2023 13:45:00 GMT+0545").getTime(),
        t = new Date("Dec 01, 2023 13:45:00 GMT+0545").getTime(),
        o = new Date().getTime();
      return o >= e && o < t;
    }
    function d() {
      p() &&
        (!(function (e) {
          o();
          const t = setInterval(o, 1e3);
          function o() {
            let o = new Date().getTime();
            const n = e - o;
            let r = Math.floor(n / 864e5),
              a = Math.floor((n % 864e5) / 36e5),
              i = Math.floor((n % 36e5) / 6e4),
              s = Math.floor((n % 6e4) / 1e3);
            o > e && ((r = 0), (a = 0), (i = 0), (s = 0), clearInterval(t)),
              r < 10 && (r = "0" + r),
              a < 10 && (a = "0" + a),
              i < 10 && (i = "0" + i),
              s < 10 && (s = "0" + s),
              $("#sale-time-countdown").html(
                r + "d : " + a + "hrs : " + i + "mins : " + s + "s"
              );
          }
        })(new Date("Dec 01, 2023 13:45:00 GMT+0545").getTime()),
        $("#sale-top-banner").removeClass("d-none"));
    }
    var u = o(1),
      m = o.n(u);
    const g = (e) => {
        const t = new Date(),
          o = new Date(t.setHours(t.getHours() + 24));
        h("showSalePopup", e, o);
      },
      h = (e, t, o = 1) => {
        m.a.set(e, t, { expires: o });
      },
      f = (e) => m.a.get(e);
    ace.define(
      "ace/mode/programiz_terminal_highlight_rules",
      function (e, t, o) {
        var n = e("ace/lib/oop"),
          r = e("ace/mode/text_highlight_rules").TextHighlightRules,
          a = function () {
            this.$rules = {
              start: [
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "(?:^|\\b)gcc($|\\s.*$)",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(/tmp).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: /^g\+\+.*$/,
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: /^cat.*$/,
                  caseInsensitive: !0,
                },
                { token: ["comment.line.colons.dosbatch"], regex: /^>/ },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(java -cp).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(csc|mono).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(node).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(swift).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(Rscript).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(go run).*$",
                  caseInsensitive: !0,
                },
                {
                  token: ["comment.line.colons.dosbatch"],
                  regex: "^(php).*$",
                  caseInsensitive: !0,
                },
              ],
            };
          };
        n.inherits(a, r), (t.ProgramizTerminalHighlightRules = a);
      }
    ),
      ace.define("ace/mode/programiz_terminal", function (e, t, o) {
        var n = e("ace/lib/oop"),
          r = e("ace/mode/text").Mode,
          a = e(
            "ace/mode/programiz_terminal_highlight_rules"
          ).ProgramizTerminalHighlightRules,
          i = function () {
            this.HighlightRules = a;
          };
        n.inherits(i, r), function () {}.call(i.prototype), (t.Mode = i);
      });
    const v = ace.edit("editor"),
      b = ace.edit("terminal");
    let w = $("#root").data("lang") || i.DEFAULT_LANGUAGE,
      k = i.ACE_EDITOR_MODES[w];
    v.setTheme("ace/theme/textmate"),
      v.getSession().setMode("ace/mode/" + k),
      b.setTheme("ace/theme/textmate"),
      b.getSession().setMode("ace/mode/programiz_terminal");
    const P = () => {
      let e = 0;
      (navigator && navigator.platform
        ? [
            "iPad Simulator",
            "iPhone Simulator",
            "iPod Simulator",
            "iPad",
            "iPhone",
            "iPod",
          ].includes(navigator.platform)
        : navigator.userAgent &&
          -1 == navigator.userAgent.toLowerCase().indexOf("iphone")) &&
        (e = 216);
      const t = ($(".wrapper").height() - 48 - 48 - e) / 22 - 3;
      v.setOptions({
        fontFamily: "droid_sans_monoregular",
        fontSize: "14px",
        showGutter: !0,
        highlightActiveLine: !0,
        wrap: !0,
        useWorker: !1,
        overwrite: !1,
        tooltipFollowsMouse: !1,
        maxLines: t,
        dragEnabled: !1,
        showPrintMargin: !1,
      }),
        (v.container.style.lineHeight = "22px"),
        b.setOptions({
          fontFamily: "droid_sans_monoregular",
          fontSize: "14px",
          showGutter: !1,
          highlightActiveLine: !1,
          behavioursEnabled: !1,
          wrapBehavioursEnabled: !1,
          wrap: !0,
          useWorker: !0,
          overwrite: !1,
          maxLines: t,
          dragEnabled: !1,
          cursorStyle: "slim",
          showPrintMargin: !1,
        }),
        (b.container.style.lineHeight = "22px"),
        c(),
        d();
    };
    P(), $(window).resize(P);
    let S = !1;
    const y = new URLSearchParams(window.location.search).get("ref");
    let A = "";
    try {
      const e = localStorage.getItem("playground"),
        t = JSON.parse(e);
      t && y && t[y] && t[y].code && ((A = t[y].code), v.setValue(A, 1));
    } catch (e) {
      localStorage.removeItem("playground");
    }
    v.commands.addCommand({
      name: "executeCode",
      bindKey: { win: "Ctrl-Enter", mac: "Cmd-Enter|Ctrl-Enter" },
      exec: function () {
        return _(), !1;
      },
    }),
      b.commands.addCommand({
        name: "backspace",
        bindKey: { win: "Backspace", mac: "Backspace|Delete" },
        exec: function () {
          return !(b.getValue().length > T.length);
        },
      }),
      b.commands.addCommand({
        name: "executeCode",
        bindKey: { win: "Ctrl-Enter", mac: "Cmd-Enter|Ctrl-Enter" },
        exec: function () {
          return _(), !1;
        },
      }),
      window.innerWidth < 1e3 &&
        ((v.renderer.$cursorLayer.isBlinking = !1),
        (b.renderer.$cursorLayer.isBlinking = !1));
    let E = null,
      T = w == i.SUPPORTED_LANGUAGES.PYTHON ? "> " : "$ ",
      C = "";
    b.commands.addCommand({
      name: "newLine",
      bindKey: { win: "Enter", mac: "Enter" },
      exec: () => (
        (C = b.getValue().slice(T.length)),
        x(),
        E.emit("evaluate", { code: C }),
        !1
      ),
    }),
      (function (e, t) {
        E = io(`${e}/?sessionId=${t}&lang=${w}`, { transports: ["websocket"] });
        const o = () => {
          $(".mobile-run-button #loader").replaceWith(a),
            $(".desktop-run-button #loader").replaceWith(a),
            $(".mobile-top-bar-run-button")
              .html
              //   '<img\n      src="assets/icons/play.svg" alt="run-icon"\n    />'
              (),
            $(".desktop-run-button").attr("disabled", !1),
            $(".desktop-run-button").css({ cursor: "pointer" });
        };
        E.on("output", ({ output: e }) => {
          o(),
            (e = e.split(">>>").join(">")),
            C.length > 0 &&
              (e.startsWith(C)
                ? ((e = e.slice(C.length)), (C = ""))
                : C.startsWith(e)
                ? ((C = C.slice(e.length)), (e = ""))
                : e.startsWith("> ") &&
                  e.replace("> ", "").startsWith(C) &&
                  (e = e.slice(C.length + 2).trimLeft())),
            0 === C.trim().length && (e = e.trimLeft());
          const t = b.getValue() + e;
          b.setValue(t, 1), (T = b.getValue()), b.focus();
        }),
          E.on("disconnect", function () {}),
          E.on("connect", function () {
            b.setValue(T, 1),
              Object.values(i.SUPPORTED_LANGUAGES).includes(w) ||
                alert(
                  `This language is not supported, initializing ${i.DEFAULT_LANGUAGE} instead`
                );
          }),
          $(".spinner").hide(),
          $(".wrapper").css({ display: "block" }),
          $(".mobile-nav-drawer").addClass("show");
      })(
        "https://" + w + ".repl-web.programiz.com",
        ((e) => {
          for (
            var t = "",
              o =
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
              n = o.length,
              r = 0;
            r < e;
            r++
          )
            t += o.charAt(Math.floor(Math.random() * n));
          return t;
        })(10)
      );
    const x = () => {
        $(".desktop-run-button").attr("disabled", !0),
          $(".desktop-run-button").css({ cursor: "not-allowed" });
      },
      _ = () => {
        (T = ""), (C = ""), G(), x(), b.setValue("");
        const e = v.getValue();
        E.emit("run", { code: e }), D(6e3);
      };
    Mousetrap.bind(["command+enter", "ctrl+enter"], function (e) {
      return _(), !1;
    }),
      $("#toggle-expanded-mode-desktop").click((e) => {
        e.preventDefault(),
          $(".spinner").show(),
          $(".wrapper").css({ display: "none" }),
          $(".mobile-nav-drawer").removeClass("show"),
          (function (e = !0) {
            e
              ? ($(".container").addClass("maximized"),
                $(".toggle-expanded-mode-desktop").prop(
                  "title",
                  "Enter Fullscreen"
                ),
                (S = !0))
              : ($(".container").removeClass("maximized"),
                $(".toggle-expanded-mode-desktop").prop(
                  "title",
                  "Exit Fullscreen"
                ),
                (S = !1));
          })(!S),
          setTimeout(() => {
            $(".spinner").hide(),
              $(".wrapper").css({ display: "block" }),
              $(".mobile-nav-drawer").addClass("show");
          }, 0);
      }),
      $(".mobile-run-button").click((e) => {
        _(), U(r);
      }),
      $(".mobile-top-bar-run-button").click((e) => {
        _(), U(r);
      });
    const O = () => (
        console.log("Opening popup"),
        l() || p()
          ? (console.log("Opening sale popup"),
            $(".sale-popup").addClass("sale-popup--sale"),
            $(".sale-popup #discount-description").html(
              "Cyber Monday Sale: 60% Discount on Programiz PRO"
            ),
            $(".sale-popup .sale-container h5").html(
              "Lifetime access to all current and future PRO courses, a personalized AI mentor, and more - Sale Ends Soon!"
            ),
            $(".sale-popup a#claim-discount")
              .html("Get My Discount")
              .attr("title", "Get My Discount")
              .attr("href"),
            void (document.getElementById("sale-popup").style.display = "flex"))
          : (console.log("Opening default popup"), void s())
      ),
      G = () => {
        $("span.run-text").replaceWith("Excute");
      },
      D = (e) => {
        (() => {
          const e = f("showSalePopup");
          return !e || "false" !== e;
        })() &&
          setTimeout(() => {
            O();
          }, e);
      };
    $(".desktop-run-button").click((e) => {
      _();
    }),
      $(".close-sale-popup").click((e) => {
        (document.getElementById("sale-popup").style.display = "none"), g(!1);
      }),
      $(".close-popup").click((e) => {
        (document.getElementById("get-started-pop-up").style.display = "none"),
          g(!1);
      }),
      $(".desktop-clear-button").click((e) => {
        (() => {
          const e = w === i.SUPPORTED_LANGUAGES.PYTHON ? "> " : "";
          b.setValue(e, 1), (T = e), (C = ""), b.focus();
        })();
      }),
      $(".burger-menu-btn").click((e) => {
        e.preventDefault(), R(!0);
      }),
      $(".close-nav-btn").click((e) => {
        e.preventDefault(), R(!1);
      });
    const U = (e) => {
      e === n &&
        ($(".shell-pill").removeClass("active"),
        $(".compiler-pill").addClass("active"),
        $(".terminal-wrapper").hide(),
        $(".editor-wrapper").show(),
        v.focus(),
        v.navigateLineEnd()),
        e === r &&
          ($(".shell-pill").addClass("active"),
          $(".compiler-pill").removeClass("active"),
          $(".terminal-wrapper").show(),
          $(".editor-wrapper").hide(),
          b.focus());
    };
    function I(e = !0) {
      if (e)
        return (
          v.setTheme("ace/theme/twilight"),
          b.setTheme("ace/theme/twilight"),
          $("#logo").attr("src", "assets/logos/logo-inverted.svg"),
          $("#nav-logo").attr("src", "assets/logos/logo-inverted.svg"),
          $(".container").addClass("dark-mode"),
          void $("#toggle-dark-mode-desktop").prop("title", "Toggle light mode")
        );
      v.setTheme("ace/theme/textmate"),
        b.setTheme("ace/theme/textmate"),
        $(".container").removeClass("dark-mode"),
        $("#logo").attr("src", "assets/logos/logo.svg"),
        $("#nav-logo").attr("src", "assets/logos/logo.svg"),
        $("#toggle-dark-mode-desktop").prop("title", "Toggle dark mode");
    }
    function L() {
      const e = localStorage.getItem("playground");
      if (!e)
        return (
          w === i.SUPPORTED_LANGUAGES.PYTHON &&
          (localStorage.setItem(
            "playground",
            JSON.stringify({ darkMode: { status: !0, updatedAt: Date.now() } })
          ),
          !0)
        );
      const t = JSON.parse(e);
      return !!(t && t.darkMode && t.darkMode.status);
    }
    function R(e = !0) {
      e
        ? $(".mobile-nav-drawer").addClass("visible")
        : $(".mobile-nav-drawer").removeClass("visible");
    }
    $(".shell-pill").click(() => {
      U(r);
    }),
      $(".compiler-pill").click(() => {
        U(n);
      }),
      $("#back-button").click(() => {
        window.history.back();
      }),
      $("#toggle-dark-mode-mobile, #toggle-dark-mode-desktop").click(() => {
        const e = JSON.parse(localStorage.getItem("playground")) || {},
          t = L() ? 0 : 1;
        let o = { status: t, updatedAt: Date.now() };
        const n = Object.assign(e, { darkMode: o });
        I(t), localStorage.setItem("playground", JSON.stringify(n));
      }),
      L() && I(!0),
      $("img.svg").each(function () {
        var e = $(this),
          t = e.attr("id"),
          o = e.attr("class"),
          n = e.attr("src");
        $.get(
          n,
          function (n) {
            var r = $(n).find("svg");
            void 0 !== t && (r = r.attr("id", t)),
              void 0 !== o && (r = r.attr("class", o + " replaced-svg")),
              (r = r.removeAttr("xmlns:a")),
              e.replaceWith(r);
          },
          "xml"
        );
      }),
      $(".desktop-save-button").on("click", () => {});
  },
]);
