import ftplib
import os
import ssl

# ==========================================
# CONFIGURAÇÕES DA HOSTINGER
# ==========================================
FTP_HOST = "ftp.areadocliente.kallalexandre.com"
FTP_USER = "u307709166.clientesprospectados"
FTP_PASS = "clientesprospectados"
PASTA_DESTINO = "/home/u307709166/domains/areadocliente.kallalexandre.com/public_html/clientes"
# ==========================================

def publicar_sites():
    print("A iniciar ligação encriptada à Hostinger...")
    
    try:
        ftp = ftplib.FTP_TLS(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.prot_p() 
        print("Ligação estabelecida com sucesso!")
        
        try:
            ftp.cwd(PASTA_DESTINO)
        except ftplib.error_perm:
            print(f"A preparar diretório base: {PASTA_DESTINO}...")
            pastas = PASTA_DESTINO.split('/')
            for p in pastas:
                try:
                    ftp.cwd(p)
                except ftplib.error_perm:
                    ftp.mkd(p)
                    ftp.cwd(p)
                    
        pasta_local = "sites"
        if not os.path.exists(pasta_local):
            print(f"A pasta '{pasta_local}' está vazia. Corra o /redesenhar primeiro.")
            return

        print("A transferir as landing pages otimizadas...")
        for raiz, _, arquivos in os.walk(pasta_local):
            for arquivo in arquivos:
                if arquivo.endswith(".html"):
                    caminho_local = os.path.join(raiz, arquivo)
                    print(f"-> A publicar: {arquivo}")
                    with open(caminho_local, 'rb') as f:
                        ftp.storbinary(f'STOR {arquivo}', f)
                        
        ftp.quit()
        print("Deploy concluído! As páginas estão ativas com sucesso.")
        
    except Exception as e:
        print(f"Falha técnica na publicação: {e}")

if __name__ == "__main__":
    publicar_sites()
