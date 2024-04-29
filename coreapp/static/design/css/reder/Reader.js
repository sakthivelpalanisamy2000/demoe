"use strict";
const _0x225f07 = _0x1d2d;
function _0x1d2d(_0x168680, _0x2dcd67) {
  const _0x6e7069 = _0x6e70();
  return (
    (_0x1d2d = function (_0x1d2d39, _0x561c08) {
      _0x1d2d39 = _0x1d2d39 - 0xf2;
      let _0x550ffe = _0x6e7069[_0x1d2d39];
      return _0x550ffe;
    }),
    _0x1d2d(_0x168680, _0x2dcd67)
  );
}
(function (_0x2199b9, _0x199240) {
  const _0x43303b = _0x1d2d,
    _0x5415dd = _0x2199b9();
  while (!![]) {
    try {
      const _0x19e85a =
        -parseInt(_0x43303b(0x100)) / 0x1 +
        -parseInt(_0x43303b(0x120)) / 0x2 +
        parseInt(_0x43303b(0xf9)) / 0x3 +
        parseInt(_0x43303b(0x114)) / 0x4 +
        -parseInt(_0x43303b(0x10c)) / 0x5 +
        (-parseInt(_0x43303b(0x127)) / 0x6) *
          (-parseInt(_0x43303b(0x10e)) / 0x7) +
        -parseInt(_0x43303b(0xf3)) / 0x8;
      if (_0x19e85a === _0x199240) break;
      else _0x5415dd["push"](_0x5415dd["shift"]());
    } catch (_0x81c25a) {
      _0x5415dd["push"](_0x5415dd["shift"]());
    }
  }
})(_0x6e70, 0x7cbec);
class Reader {
  #element;
  #voices;
  static ["id"] =
    "r" + Math[_0x225f07(0x115)]()[_0x225f07(0x107)](0x24)["slice"](0x2);
  #textContent;
  #is_highlightable;
  #highlightColor = _0x225f07(0x106);
  #html;
  #speed = 0x1;
  #currVoice;
  #pitch = 0x1;
  #wordArr;
  #currIndex;
  constructor() {
    this.#voices = new Array();
    let _0x495087 = setInterval(() => {
      const _0x8d9376 = _0x1d2d;
      if (window[_0x8d9376(0x131)][_0x8d9376(0x132)]() != null) {
        clearInterval(_0x495087);
        let _0x3248f8 = new Array();
        window[_0x8d9376(0x131)]["getVoices"]()["forEach"]((_0x1e6e69) => {
          const _0x48d128 = _0x8d9376;
          _0x1e6e69["localService"] && _0x3248f8[_0x48d128(0x111)](_0x1e6e69);
        }),
          (this.#voices = _0x3248f8),
          (this.#currVoice = this.#voices[0x0]);
      }
    }, 0xa);
  }
  ["setHighlight"](_0x39464a) {
    this.#highlightColor = _0x39464a;
  }
  [_0x225f07(0x132)]() {
    return new Promise((_0x2c8ab0, _0x311409) => {
      let _0x13611e = setInterval(() => {
        const _0x5bb45f = _0x1d2d;
        if (window[_0x5bb45f(0x131)][_0x5bb45f(0x132)]() != null) {
          clearInterval(_0x13611e);
          let _0x8be8fe = new Array();
          window[_0x5bb45f(0x131)]
            [_0x5bb45f(0x132)]()
            ["forEach"]((_0x4ce270) => {
              const _0x37bc7b = _0x5bb45f;
              _0x4ce270[_0x37bc7b(0xf6)] &&
                _0x8be8fe[_0x37bc7b(0x111)](_0x4ce270);
            }),
            _0x2c8ab0(_0x8be8fe);
        }
      }, 0x64);
    });
  }
  [_0x225f07(0x104)](_0x6c3184) {
    const _0x537f17 = _0x225f07;
    if (typeof _0x6c3184 == _0x537f17(0x11d))
      this.#currVoice = window[_0x537f17(0x131)][_0x537f17(0x132)]()[_0x6c3184];
    else {
      if (typeof _0x6c3184 == "string") {
        (_0x6c3184 = parseInt(_0x6c3184)),
          (this.#currVoice =
            window[_0x537f17(0x131)][_0x537f17(0x132)]()[_0x6c3184]);
      } else this.#currVoice = _0x6c3184;
    }
  }
  [_0x225f07(0x12e)](_0x3e0dae) {
    this.#speed = _0x3e0dae;
  }
  [_0x225f07(0x103)](_0xaab52d) {
    this.#pitch = _0xaab52d;
  }
  [_0x225f07(0x129)](_0x2853d0) {
    this.#onboundary = _0x2853d0;
  }
  [_0x225f07(0xfd)](_0x50546c) {
    this.#onmark = _0x50546c;
  }
  ["setOnStart"](_0x50d25a) {
    this.#onstart = _0x50d25a;
  }
  [_0x225f07(0x123)](_0x463d23) {
    this.#onpause = _0x463d23;
  }
  [_0x225f07(0xfa)](_0x48c395) {
    this.#onresume = _0x48c395;
  }
  [_0x225f07(0x12d)](_0x5c5cfc) {
    this.#onerror = _0x5c5cfc;
  }
  #onend = () => {};
  #onpause = () => {};
  #onresume = () => {};
  #onstart = () => {};
  #onmark = () => {};
  #onboundary = () => {};
  #onerror = (_0x2a7e9a) => {
    const _0x20dcd1 = _0x225f07;
    console["error"](_0x20dcd1(0x11b), _0x2a7e9a);
  };
  [_0x225f07(0x133)](_0x14feba) {
    const _0x2f3003 = _0x225f07;
    this[_0x2f3003(0x10f)](),
      (this.#element = _0x14feba),
      (this.#textContent = this.#element["value"]
        ? this.#element[_0x2f3003(0x10b)]
        : this.#element[_0x2f3003(0x110)]),
      (this.#is_highlightable = this.#element[_0x2f3003(0x110)] ? !![] : ![]),
      (this.#html = this.#element[_0x2f3003(0xf7)]),
      this.#is_highlightable
        ? ((this.#wordArr = [0x0]["concat"](
            this.#itterate(0x0, this.#element[_0x2f3003(0xf7)][_0x2f3003(0xfc)])
          )),
          (this.#currIndex = 0x0))
        : (this.#wordArr = null);
  }
  ["readWhen"](_0x517478, _0x5ba50b) {
    const _0x217983 = _0x225f07;
    _0x5ba50b[_0x217983(0x12a)](_0x517478, () => {
      this["setElement"](_0x5ba50b), this["read"]();
    });
  }
  [_0x225f07(0x116)] = window["speechSynthesis"][_0x225f07(0x116)];
  [_0x225f07(0xfb)] = window["speechSynthesis"][_0x225f07(0xfb)];
  [_0x225f07(0x118)]() {
    const _0x463d32 = _0x225f07;
    this["cancel"]();
    let _0x1f6af3 = new SpeechSynthesisUtterance(this.#textContent);
    (_0x1f6af3[_0x463d32(0x125)] = this.#currVoice),
      (_0x1f6af3[_0x463d32(0x12c)] = this.#speed),
      (_0x1f6af3[_0x463d32(0x10d)] = 0x1),
      (_0x1f6af3["pitch"] = this.#pitch),
      this.#is_highlightable &&
        ((_0x1f6af3[_0x463d32(0xf5)] = (_0x52fd4d) => {
          const _0x5a0495 = _0x463d32;
          this.#onboundary(),
            _0x52fd4d["name"] == "word" &&
              this.#changeWord(
                this.#textContent[_0x5a0495(0xf8)](
                  _0x52fd4d[_0x5a0495(0x128)],
                  _0x52fd4d[_0x5a0495(0x128)] + _0x52fd4d["charLength"]
                )
              );
        }),
        (_0x1f6af3[_0x463d32(0x10a)] = this.#onpause),
        (_0x1f6af3[_0x463d32(0x11c)] = this.#onresume),
        (_0x1f6af3[_0x463d32(0x126)] = this.#onstart),
        (_0x1f6af3[_0x463d32(0xf2)] = this.#onerror),
        (_0x1f6af3[_0x463d32(0x121)] = this.#onmark),
        (_0x1f6af3["onend"] = () => {
          this.#onend(),
            (this.#element["innerHTML"] = this.#html),
            (this.#currIndex = -0x1);
        })),
      window["speechSynthesis"][_0x463d32(0x112)](_0x1f6af3);
  }
  [_0x225f07(0x10f)]() {
    const _0x11b97e = _0x225f07;
    window[_0x11b97e(0x131)][_0x11b97e(0x10f)](), (this.#currIndex = 0x0);
    let _0x3fee45 = Array[_0x11b97e(0x11f)](
      document[_0x11b97e(0x101)]("." + Reader["id"])
    );
    _0x3fee45[_0x11b97e(0x12b)]((_0x27767f, _0x47adf9) => {
      const _0x53cc93 = _0x11b97e;
      _0x3fee45[_0x47adf9]["outerHTML"] = _0x27767f[_0x53cc93(0x110)];
    });
  }
  [_0x225f07(0x124)](_0x596e9f) {
    let _0x534004 = setInterval((_0x379136) => {
      const _0x3dc5e6 = _0x1d2d;
      !window["speechSynthesis"][_0x3dc5e6(0x11a)] &&
        (console[_0x3dc5e6(0x122)]("not\x20reading!!"),
        clearInterval(_0x534004),
        this[_0x3dc5e6(0x133)](_0x596e9f),
        this[_0x3dc5e6(0x118)]());
    }, 0x64);
  }
  static #cleanString(_0xf809e3) {
    const _0x50bc7e = _0x225f07;
    let _0x55a962 = new RegExp(_0x50bc7e(0x108)),
      _0x1ff554 = "";
    while (_0xf809e3 != _0x1ff554) {
      (_0x1ff554 = _0xf809e3),
        (_0xf809e3 = _0xf809e3[_0x50bc7e(0xff)](_0x55a962, ""));
    }
    return _0xf809e3;
  }
  #itterate(_0x32c60e, _0x4bdbe5) {
    const _0x2135e9 = _0x225f07;
    let _0x2a1f1a = new Array();
    while (_0x32c60e < _0x4bdbe5) {
      if (this.#html[_0x32c60e] == "\x20" || this.#html[_0x32c60e] == "\x0a")
        _0x32c60e++;
      else {
        if (this.#html[_0x32c60e] == "<") {
          let _0x2f79d0 = this.#html[_0x2135e9(0x11e)](">", _0x32c60e);
          (_0x32c60e = _0x2f79d0 + 0x1),
            _0x2a1f1a[_0x2135e9(0x111)](_0x2f79d0 + 0x1);
        } else {
          let _0x85d003 = this.#html[_0x2135e9(0x11e)]("\x20", _0x32c60e),
            _0x47337d = this.#html["indexOf"]("<", _0x32c60e);
          if (_0x85d003 > _0x47337d && _0x47337d != -0x1) {
            let _0x2e0012 = [
              _0x47337d,
              this.#html[_0x2135e9(0x11e)](">", _0x47337d) + 0x1,
            ];
            _0x2a1f1a[_0x2135e9(0x111)](_0x2e0012[0x0]);
            if (_0x2e0012[0x1] == 0x0) {
              _0x2a1f1a["push"](this.#html["length"] + 0x1);
              break;
            }
            _0x2a1f1a[_0x2135e9(0x111)](_0x2e0012[0x1]),
              (_0x32c60e = _0x2e0012[0x1]);
          } else {
            if (_0x85d003 != -0x1)
              _0x2a1f1a[_0x2135e9(0x111)](_0x85d003 + 0x1),
                (_0x32c60e = _0x85d003 + 0x1);
            else {
              if (_0x47337d != -0x1)
                _0x2a1f1a[_0x2135e9(0x111)](_0x47337d),
                  (_0x32c60e =
                    this.#html[_0x2135e9(0x11e)](">", _0x47337d) + 0x1);
              else {
                _0x2a1f1a[_0x2135e9(0x111)](this.#html[_0x2135e9(0xfc)] + 0x1);
                break;
              }
            }
          }
        }
      }
    }
    return _0x2a1f1a;
  }
  #changeWord(_0x437e88) {
    const _0xc1e9a7 = _0x225f07;
    if (this.#currIndex == this.#wordArr["length"] - 0x1) {
      (this.#currIndex = -0x1), (this.#element[_0xc1e9a7(0xf7)] = this.#html);
      return;
    }
    this.#html
      ["substring"](
        this.#wordArr[this.#currIndex],
        this.#wordArr[this.#currIndex + 0x1]
      )
      [_0xc1e9a7(0x12f)]("<") && (this.#currIndex++, this.#changeWord()),
      this.#element != null &&
        this.#currIndex != -0x1 &&
        this.#html
          [_0xc1e9a7(0xf8)](
            this.#wordArr[this.#currIndex],
            this.#wordArr[this.#currIndex + 0x1]
          )
          [_0xc1e9a7(0x11e)](_0x437e88) != -0x1 &&
        ((this.#element[_0xc1e9a7(0xf7)] =
          this.#html[_0xc1e9a7(0xf8)](0x0, this.#wordArr[this.#currIndex]) +
          _0xc1e9a7(0x109) +
          Reader["id"] +
          _0xc1e9a7(0x130) +
          this.#highlightColor +
          _0xc1e9a7(0x105) +
          this.#html["substring"](
            this.#wordArr[this.#currIndex],
            this.#wordArr[this.#currIndex + 0x1]
          ) +
          _0xc1e9a7(0x113) +
          this.#html[_0xc1e9a7(0xf8)](this.#wordArr[this.#currIndex + 0x1])),
        this.#currIndex++);
  }
  [_0x225f07(0xfe)]() {
    const _0x58184d = _0x225f07;
    window[_0x58184d(0x117)](_0x58184d(0x119), _0x58184d(0x102));
  }
  [_0x225f07(0xf4)]() {
    const _0x59ac6f = _0x225f07;
    window[_0x59ac6f(0x117)](
      "https://foureyedjimmy.com/contact?p=reader&r=bug/suggestion"
    );
  }
}
function _0x6e70() {
  const _0x222467 = [
    "report",
    "onboundary",
    "localService",
    "innerHTML",
    "substring",
    "1512054tVCqIJ",
    "setOnResume",
    "resume",
    "length",
    "setOnMark",
    "docs",
    "replace",
    "245174vhgcHL",
    "querySelectorAll",
    "_blank",
    "setPitch",
    "setVoice",
    ";\x22>",
    "lightblue",
    "toString",
    "\x20|\x0a",
    "<c\x20class=\x22",
    "onpause",
    "value",
    "2071835DJcLMv",
    "volume",
    "413XwYarO",
    "cancel",
    "textContent",
    "push",
    "speak",
    "</c>",
    "2355128uYKjwq",
    "random",
    "pause",
    "open",
    "read",
    "https://code.foureyedjimmy.com/reader/docs",
    "speaking",
    "an\x20utterance\x20error\x20occured:",
    "onresume",
    "number",
    "indexOf",
    "from",
    "1194414xgGqMD",
    "onmark",
    "log",
    "setOnPause",
    "readOnFinish",
    "voice",
    "onstart",
    "98634FlEzAX",
    "charIndex",
    "setOnBoundary",
    "addEventListener",
    "forEach",
    "rate",
    "setOnError",
    "setSpeed",
    "includes",
    "\x22\x20style=\x22background:\x20",
    "speechSynthesis",
    "getVoices",
    "setElement",
    "onerror",
    "2359976tGFJeq",
  ];
  _0x6e70 = function () {
    return _0x222467;
  };
  return _0x6e70();
}
