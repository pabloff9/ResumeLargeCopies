#!-*- coding: utf8 -*-
#! /usr/bin/env python2

"""
Esse programa serve para continuar a cópia de um arquivo de onde ela parou.
Isso é útil para cópias de arquivos grandes que falharam no meio.
"""
import os.path
from gi.repository import Gtk, Gdk

class Application():
    
    arquivoOriginal = None
    arquivoIncompleto = None
    
    def __init__(self):
        
        endereco = input("Digite o endereço do arquivo original.\n")
        self.arquivoOriginal = open(endereco, mode="rb")
        endereco = input("Digite o endereco do arquivo incompleto.\n")
        self.arquivoIncompleto = open(endereco, mode="ab")
        self.doWork()
        
        
#        # Pegando o endereço do arquivo original do clipboard e abrindo o arquivo para leitura
#        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
#        self.arquivoOriginal = open(clipboard.wait_for_text(), mode="rb")
#        
#        # Abrindo o arquivo de destino, que deve ter o mesmo nome do arquivo original
#        arquivoDeDestino = os.environ["NAUTILUS_SCRIPT_CURRENT_URI"] + self.arquivoOriginal.name
#        self.arquivoIncompleto = open(arquivoDeDestino, mode="ab")
#        
#        self.doWork()
        
        print("\nTrabalho concluído!\n")
        
    def doWork(self):
        
        #Descobrindo o tamanho do arquivo incompleto e posicionando o cursor 
        #Na posição correspondente do arquivo original
        tamanhoDoArquivoIncompleto = os.path.getsize(self.arquivoIncompleto.name)
        self.arquivoOriginal.seek(tamanhoDoArquivoIncompleto)
        
        #Agora começamos a escrever no fim do arquivo imcompleto todos os bytes do arquivo original
        #que puderem ser lidos a partir dessa posicao do cursor, 4KB por vez (para tomar proveito da bufferização da escrita em disco)
        pedaco = self.arquivoOriginal.read(4096)
        while (pedaco != b""):
            self.arquivoIncompleto.write(pedaco)
            pedaco = self.arquivoOriginal.read(4096)
            
    
Application()
    
        
        
