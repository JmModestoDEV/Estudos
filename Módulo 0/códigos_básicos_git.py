print(f"""
git config --global user.name "nome do usuario" (Adiciona o nome do usuario que deve ser o mesmo do seu github)
git config --global user.email "email do usuario"(adiciona o email que deve ser o mesmo do seu github)
git config --list - Lista as configs atuais 
git init - Cria o repositório local no seu pc
git add arquivo.txt - Adiciona um arquivo especifico no repositorio local     
git add . - Adiciona todos os arquivos do projeto no repositorio local
git commit -m "Mensagem do commit" - Utilizado para explicar as alterações feitas nesse comit
git status - verificar os status dos arquivos
git diff - verificar as alterações feitas
git branch -M main - transforma o nome da raiz do seu projeto para Main ao inves do antigo modelo chamado de master 
git remote add origin git@github.com:seuusuario/seurepositorio.git - utilizado para dar acesso ao repositorio online do github
git push - envia os arquivos do repositorio local para o repositorio remoto do github
""")
