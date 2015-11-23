var counter = 1;
var limit = 60;
function addInput(divName){
    if (counter == limit)  {
        alert("You have reached the limit of adding " + counter + " inputs");
    }
    else {
        var section = document.getElementById(divName);
        var newdiv = document.createElement('div');
        newdiv.innerHTML = "<br><input type='text' name='operator" + (counter + 1) + "' placeholder='Operator Id' class='form-control'>" + "<input type='text' name='margin" + (counter + 1) + "' placeholder='Margin' class='form-control' style='margin-left:10px;'>";
        section.insertBefore(newdiv, section.firstChild);
        document.getElementById('counter').value++;
        counter++;
    }
}