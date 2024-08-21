var QRCODE_TEXT = ''

function startDeposit(){
    document.getElementById('deposit_select_modal').style.display = 'block'
}

function close_deposit(){
    document.getElementById('deposit_page').style.display = 'none'
}

function open_deposit(){
document.getElementById('deposit_page').style.display = 'block'
}

function copyQR(){
    const button = document.getElementById('copy-qrcode')
    navigator.clipboard.writeText(QRCODE_TEXT)
    button.innerHTML = 'qrcode copiado'
    setTimeout(function(){button.innerHTML = 'Copiar qrcode'}, 5000)

}

function requireQRCODE(value){
    document.getElementById('deposit_loader').style.display = 'block'
    var http = new XMLHttpRequest();
    var url = '/get_qr';
    var params = JSON.stringify({value:value});
    http.open('POST', url, true);

    //Send the proper header information along with the request
    http.setRequestHeader('Content-type', 'application/json');

    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            document.getElementById('deposit_select_modal').style.display = 'none'
            document.getElementById('deposit_loader').style.display = 'none'
            open_deposit()           
            
            
            
            args = JSON.parse(http.responseText)
            console.log(args)
            if(args['code']==200){
                QRCODE_TEXT = args['text']
                document.getElementById('qrcode').style.backgroundImage = 'url("/qr/'+args['id']+'")'
                document.getElementById('deposit-value').innerHTML = 'R$'+value
            }




        }
    }
    http.send(params);

}


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