const output = document.getElementById("output");
const input = document.getElementById("code");
const scriptHolder = document.getElementById("script-holder");


console.log = (data) =>  {
    output.innerHTML += data + '<br>';
}

console.error = (err) => {
    output.innerHTML += `<div class=error>${err}</div>`
}

document.getElementById("code-submit").addEventListener("click", () => {
    let script = document.createElement("script");
    script.type="text/javascript";
    script.textContent = input.value;
    scriptHolder.innerHTML = null;
    scriptHolder.append(script);
})

document.getElementById("clear").addEventListener('click', () =>{
    console.log("running");
    output.innerText = null;
});

document.querySelectorAll(".code").forEach(el => {
    el.addEventListener("keydown", (e) => {
        if(e.key == 'Tab'){
            e.preventDefault();
            let start = el.selectionStart;
            el.value = `${el.value.substring(0, el.selectionStart)}\t${el.value.substring(el.selectionStart)}`;
            el.selectionStart = start + 1;
            el.selectionEnd = el.selectionStart;
            
        }
    })
})

