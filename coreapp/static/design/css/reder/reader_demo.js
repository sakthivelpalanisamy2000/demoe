
const control = document.querySelector(".control-panel");

Array.from(document.querySelectorAll(".clickable")).forEach(el => {
    el.addEventListener("click" , () => {
        read(el);
    });
})

function read(el){
    let reader = new Reader();
    reader.setVoice(control["voice"].value);
    reader.setPitch(control["pitch"].value);
    reader.setSpeed(control["speed"].value);
    reader.setHighlight(control["toggle"].checked ? control["color"].value : "none");
    reader.setElement(el);
    reader.read();
}

function convert(){
    document.getElementById("output").innerHTML = document.getElementById("test-input").value;
}

function readbox(){
    read(document.getElementById("test-input"));
}

document.addEventListener("DOMContentLoaded", async () => {

    let reader = new Reader();
    let voices = await reader.getVoices();
    let select = document.getElementById("voices");
    
    voices.forEach((el, index) => {
        let option = document.createElement("option");
        option.value = index;
        option.textContent = el.name;
        
        select.append(option);
    })
})
