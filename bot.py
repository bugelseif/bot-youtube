# Import for the Web Bot
from webdriver_manager.firefox import GeckoDriverManager
# Import de Web Bot
from botcity.web import WebBot, Browser, By

# Import de integração com BotCity Maestro SDK
from botcity.maestro import *

# Desativa mensagem de erros por não estar conectado ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Instancia do BotMaestroSDK
    maestro = BotMaestroSDK.from_sys_args()
    # Objeto com informações da execução
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configuração do modo headless
    bot.headless = False

    # Configuração do navegador
    bot.browser = Browser.FIREFOX

    # Caminho para o webdriver
    bot.driver_path = GeckoDriverManager().install()

    # Lista de canais para pesquisar
    canais = ['botcity_br', 'botcity-dev', 'youtube', 'github']

    for canal in canais:
        # Inicia o navegador
        bot.browse(f"https://www.youtube.com/@{canal}")

        # Retorna lista de elementos
        element = bot.find_elements(selector='//span[@class="yt-core-attributed-string yt-content-metadata-view-model-wiz__metadata-text yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--link-inherit-color" and @role="text"]', by=By.XPATH)

        # Captura o texto de cada elemento
        nome_canal = element[0].text
        numero_inscritos = element[1].text
        quantidade_videos = element[2].text
        print(f"Nome do canal: {nome_canal} | Número de inscritos: {numero_inscritos} | Quantidade de vídeos: {quantidade_videos}")


        # Finaliza o navegador
        bot.wait(3000)
        bot.stop_browser()

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Tarefa BotYoutube finalizada com sucesso",
        total_items=1, # Número total de itens processados
        processed_items=1, # Número de itens processados com sucesso
        failed_items=0 # Número de itens processados com falha
    )



if __name__ == '__main__':
    main()