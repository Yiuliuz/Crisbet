class Impresora():
    def __init__(self):
        self.ruta_word_config="{}\\config.docx".format(getcwd())
        self.ruta_word_temp="{}\\imprimir.docx".format(cesar.ruta_temporales)
    def imprimir(self,parrafo):
        operative_sist.copiar_archivo(self.ruta_word_config,self.ruta_word_temp)
        archivo=Document(self.ruta_word_temp)
        a=archivo.add_paragraph
        run=a.add_run(parrafo)
        font=run.font
        font.size=Pt(8)
        archivo.save(ruta)
        subprocess.Popen(["C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE","/t",self.ruta_word_temp,"/mArchivoImprimirPredeter","/mArchivoCerrarOSalir"])
        operative_sist.eliminar_archivo(self.ruta_word_temp)