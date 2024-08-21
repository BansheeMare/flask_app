
function login(){
    setTimeout(function(){
    document.getElementById('balance').style.display = 'block'
    document.getElementById('usuario').style.display = 'block'
    document.getElementById('depos').style.display = 'block'
    document.getElementById('usuario').innerHTML = document.getElementById('username').value
    document.getElementById('login_screen').style.display = 'none'

    setTimeout(function(){startDeposit()}, 500)
}, 1500)

}

function game(){
    document.getElementById('alert').style.display = 'block'
    document.getElementById('alert').style.opacity = 1
    setTimeout(function(){

        document.getElementById('alert').style.display = 'none'
        document.getElementById('alert').style.opacity = 0


    }, 2000)

}