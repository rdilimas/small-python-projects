from winotify import Notification, audio

notificacao = Notification(app_id="Minha primeira Notificação", 
                           title="Titulo da Notificação", 
                           msg="Mensagem disparada, cuidado pra não Prolongar muito aqui!!!",
                           duration="short", icon=r"C:\small-python-projects\08 - Notificação do Sistema\logo.png")
                           


notificacao.set_audio(audio.LoopingCall9, loop=False)
notificacao.add_actions(label="Ver mais Inforções", launch="https://pypi.org/project/winotify/")
notificacao.show()
