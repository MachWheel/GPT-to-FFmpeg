APP_NAME = "GPT to FFmpeg  v1.2"
INPUT_FILE_NEEDED_ERROR = "Você precisa selecionar um arquivo de entrada primeiro"
PROMPT_NEEDED_ERROR = 'Diga como quer converter ou alterar o arquivo primeiro\n\nExemplo:\n"Quero só o áudio deste vídeo em .mp3"'
NO_MIC_ERROR = "Parece que não existe nenhum microfone selecionado por padrão no seu computador."
LISTENING_ERROR = 'Não consegui entender o que você disse.'
WAIT_TIMEOUT_ERROR = 'Não ouvi o que você disse.'
LISTENING_REQUEST_ERROR = 'Desculpe, não consigo reconhecer sua voz no momento.; {0}'
LISTENING_VOICE = 'Fale o que você precisa...'
DOWNLOADING_FFMPEG = 'Baixando ffmpeg...'
GPT_REQUEST_PROMPT = "Você faz parte de um script Python que permite realizar conversões de áudio e vídeo, utilizando o ffmpeg, em um computador rodando Windows.\n\
Atenção: Sua resposta será DIRETAMENTE executada em um terminal do Windows.\n\
Portanto, eu preciso que, independente do que seja pedido pelo usuário, sua resposta contenha ESTRITAMENTE APENAS UM COMANDO FFMPEG PARA SER EXECUTADO, SEM NENHUMA FORMATAÇÃO OU MARKUP!\n\
Sabendo disso, este é o pedido do usuário:\n\n\
{prompt}\n\
O arquivo que será utilizado é este aqui:\n\
\"{input_file}\"\n\
O arquivo de saída deve ser gerado no mesmo diretório do arquivo de entrada, com o prefixo \"gpt_\" em seu nome."
GPT_UNAVAILABLE_ERROR = "Serviço do OpenAI sobrecarregado ou indisponível no momento"
GPT_AUTH_ERROR = "Erro de autenticação:\nA API key salva é inválida e será apagada.\nO programa será encerrado."
FILE_BROWSE_TEXT = "1. Selecione o arquivo de entrada:"
FILE_BROWSE_BUTTON = "Procurar arquivo..."
CONVERT_PROMPT_TEXT = "2. Diga como quer converter ou alterar o arquivo:"
VIEW_HISTORY = "...ou selecione a partir do seu histórico"
VOICE_COMMAND = "Escrever com a minha voz"
EXECUTE_TEXT = "Iniciar"
NO_SELECTED_FILE = "Nenhum arquivo de entrada selecionado ainda"
FOOTER_NOTE = 'O arquivo é exportado no mesmo diretório da entrada,\ncom o prefixo "gpt_" em seu nome'
EXPORTED_SUCCESS_MSG = '\nSeu arquivo foi gerado com sucesso!\nA pasta com o arquivo gerado será aberta.\n'
EXPORTED_SUCCESS_BTN = 'Abrir pasta'
ENTER_PASSWORD = f'Digite sua senha para abrir o {APP_NAME}'
WELCOME = '\nSeja bem vindo\n'
INCORRECT_PASSWORD_ERROR = 'Senha incorreta. Tente novamente.'
ENTER_NEW_PASSWORD = 'Insira uma nova senha (com pelo menos 8 caracteres)'
CONFIRM_NEW_PASSWORD = 'Confirme sua senha'
PASSWORD_ERROR = 'As senhas não correspondem ou têm menos de 8 caracteres. Tente novamente.'
API_DISCLAIMER = "\nÉ necessário uma API key da OpenAI para que este programa funcione\n\n\
A chave não está presente na variável de ambiente \"OPENAI_API_KEY\".\n\n\n\
Você pode fechar o programa e definir esta variavel manualmente,\n\
ou continuar e armazenar sua chave aqui:\n\n\
Você definirá uma senha para proteger o acesso a sua chave\n\n\
Esta senha será necessária sempre que você abrir o programa\n\n\
Caso esqueça esta senha, você deverá:\n\
- Gerar uma nova API key\n\
- Definir uma nova senha\n\n"
CONTINUE = 'Continuar'
STORE_KEY_LOCALLY = 'Continuar e armazenar aqui'
QUIT = 'Sair do programa'
GO_TO_SITE = 'Ir até a página "API keys" no site da OpenAI'
ENTER_API_KEY = 'Insira sua OpenAI API key'
REMEMBER_PASSWORD = "Deseja lembrar sua senha para o próximo acesso?"
INVALID_API_KEY = 'Formato inválido da API key\nInsira sua OpenAI API key'
PASSWORD_LIMIT_ERROR = 'Limite de tentativas excedido.\n\
Por questões de segurança, a API key salva será excluída.\n\n\
Na próxima vez que abrir este programa você deverá:\n\
- Gerar e salvar uma nova API key\n\
- Definir um nova senha para o programa'
CANCELLED_OPERATION = "Operação cancelada"


def CMD_WARNING(command: str):
    return (
        f"AVISO!\n"
        f"ESTE COMANDO SERÁ EXECUTADO NO SEU TERMINAL:\n\n"
        f"{command}\n\n"
        f"Você deseja continuar?"
    )
