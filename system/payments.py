from efipay import EfiPay
import base64
import system.generate

credentials_homo = {
    'client_id': 'Client_Id_1e71435c4b28ded2bcdd3a79042cb10d6e18293a',
    'client_secret': 'Client_Secret_b5027471b3d53c99d57c564a25fdcef7c5e4b05a',
    'sandbox': True,
    'certificate': './archives/certificates/efi-homo.pem'
}
credentials_prod = {
    'client_id': 'Client_Id_c04c513f833d3ddbe76c1585cc8941aac0b5101b',
    'client_secret': 'Client_Secret_19fa09f965b82e46f565aabdf7d1c137fc7b472b',
    'sandbox': False,
    'certificate': './archives/certificates/efi-prod.pem'
}

efi = EfiPay(credentials_homo)


def get_qrcode(value:int):
    body = {
        'calendario': {
            'expiracao': 3600
        },
        'devedor': {
            'cpf': '12345678909',
            'nome': 'Francisco da Silva'
        },
        'valor': {
            'original': f'{str(value)}.00'
        },
        'chave': 'glownascimento9@gmail.com',
        'solicitacaoPagador': 'Cobrança dos serviços prestados.'
    }
    qrid = system.generate.gen_qrcode_id()
    cob =  efi.pix_create_immediate_charge(body=body)
    
    
    response =  efi.pix_generate_qrcode(params={'id':cob['loc']['id']})
    if('imagemQrcode' in response):
        with open(f'./archives/images/qrcodes/{qrid}.png', 'wb') as fh:
            fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))
            return {'code':200, 'id':qrid, 'text':response['qrcode']}
        
    
