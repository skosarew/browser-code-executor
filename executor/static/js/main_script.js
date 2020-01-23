// document.getElementById('code-container').innerText = document.getElementById('code-container-hidden').value;

function refresh_code(){
    document.getElementById('code-container-hidden').value = window.editor.getValue();
}
