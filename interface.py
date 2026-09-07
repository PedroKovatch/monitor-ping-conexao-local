import tkinter as tk
from datetime import datetime
from threading import Thread
from tkinter import messagebox, ttk

from dados import (
    adicionar_filial,
    carregar_filiais,
    editar_filial,
    excluir_filial,
)
from monitoramento import testar_ping


COR_FUNDO = "#1E1E1E"
COR_SUPERFICIE = "#252526"
COR_CABECALHO = "#333333"
COR_TEXTO = "#F3F3F3"
COR_TEXTO_SECUNDARIO = "#B8B8B8"
COR_SELECAO = "#264F78"
COR_BOTAO = "#0E639C"
COR_BOTAO_ATIVO = "#1177BB"
COR_AGUARDANDO = "#D7BA7D"
COR_ONLINE = "#89D185"
COR_INDISPONIVEL = "#F14C4C"

# Intervalo entre as verificações automáticas, informado em milissegundos.
INTERVALO_ATUALIZACAO = 10000


def configurar_estilo():
    """
    Configura os estilos visuais escuros da interface.
    """
    estilo = ttk.Style()
    estilo.theme_use("clam")

    estilo.configure("TFrame", background=COR_FUNDO)

    estilo.configure(
        "Cadastro.TFrame",
        background=COR_SUPERFICIE
    )

    estilo.configure(
        "Titulo.TLabel",
        background=COR_FUNDO,
        foreground=COR_TEXTO,
        font=("Segoe UI", 18, "bold")
    )

    estilo.configure(
        "Descricao.TLabel",
        background=COR_FUNDO,
        foreground=COR_TEXTO_SECUNDARIO,
        font=("Segoe UI", 10)
    )

    estilo.configure(
        "Campo.TLabel",
        background=COR_SUPERFICIE,
        foreground=COR_TEXTO,
        font=("Segoe UI", 10)
    )

    estilo.configure(
        "TEntry",
        fieldbackground="#3C3C3C",
        foreground=COR_TEXTO,
        insertcolor=COR_TEXTO
    )

    estilo.configure(
        "Adicionar.TButton",
        background=COR_BOTAO,
        foreground=COR_TEXTO,
        borderwidth=0,
        font=("Segoe UI", 10, "bold"),
        padding=(12, 7)
    )

    estilo.map(
        "Adicionar.TButton",
        background=[("active", COR_BOTAO_ATIVO)]
    )

    estilo.configure(
        "Treeview",
        background=COR_SUPERFICIE,
        fieldbackground=COR_SUPERFICIE,
        foreground=COR_TEXTO,
        rowheight=30,
        borderwidth=0,
        font=("Segoe UI", 10)
    )

    estilo.configure(
        "Treeview.Heading",
        background=COR_CABECALHO,
        foreground=COR_TEXTO,
        font=("Segoe UI", 10, "bold"),
        relief="flat"
    )

    estilo.map(
        "Treeview",
        background=[("selected", COR_SELECAO)],
        foreground=[("selected", COR_TEXTO)]
    )

    estilo.map(
        "Treeview.Heading",
        background=[("active", "#3E3E42")]
    )


def iniciar_interface():
    """
    Cria e exibe a janela principal do Monitor de Conexão Local.
    """
    janela = tk.Tk()
    janela.title("Monitor de Conexão Local")
    janela.geometry("850x560")
    janela.minsize(700, 450)
    janela.configure(background=COR_FUNDO)

    configurar_estilo()

    conteudo = ttk.Frame(janela, padding=20)
    conteudo.pack(fill="both", expand=True)

    titulo = ttk.Label(
        conteudo,
        text="Monitor de Conexão Local",
        style="Titulo.TLabel"
    )
    titulo.pack(anchor="w")

    descricao = ttk.Label(
        conteudo,
        text="Acompanhe o status de conectividade dos roteadores cadastrados.",
        style="Descricao.TLabel"
    )
    descricao.pack(anchor="w", pady=(5, 20))

    # Variáveis ligadas aos campos de cadastro.
    nome_var = tk.StringVar()
    ip_var = tk.StringVar()
    ultima_atualizacao_var = tk.StringVar(
        value="Última atualização: aguardando"
    )

    # Informa se uma verificação de ping já está sendo executada.
    monitoramento_em_andamento = False

    # Guarda o nome original da filial que está sendo editada.
    filial_em_edicao = None

    cadastro = ttk.Frame(
        conteudo,
        padding=15,
        style="Cadastro.TFrame"
    )
    cadastro.pack(fill="x", pady=(0, 20))

    ttk.Label(
        cadastro,
        text="Filial",
        style="Campo.TLabel"
    ).grid(row=0, column=0, sticky="w")

    campo_nome = ttk.Entry(
        cadastro,
        textvariable=nome_var,
        width=30
    )
    campo_nome.grid(row=1, column=0, sticky="ew", padx=(0, 15))

    ttk.Label(
        cadastro,
        text="IP do roteador",
        style="Campo.TLabel"
    ).grid(row=0, column=1, sticky="w")

    campo_ip = ttk.Entry(
        cadastro,
        textvariable=ip_var,
        width=25
    )
    campo_ip.grid(row=1, column=1, sticky="ew", padx=(0, 15))

    cadastro.columnconfigure(0, weight=1)
    cadastro.columnconfigure(1, weight=1)

    tabela = ttk.Treeview(
        conteudo,
        columns=("status", "filial", "ip"),
        show="headings",
        height=12
    )

    tabela.heading("status", text="Status")
    tabela.heading("filial", text="Filial")
    tabela.heading("ip", text="IP do roteador")

    tabela.column("status", width=140, anchor="center")
    tabela.column("filial", width=350)
    tabela.column("ip", width=220)

    tabela.tag_configure("aguardando", foreground=COR_AGUARDANDO)
    tabela.tag_configure("online", foreground=COR_ONLINE)
    tabela.tag_configure("indisponivel", foreground=COR_INDISPONIVEL)

    def atualizar_tabela(status_por_ip=None):
        """
        Limpa a tabela e exibe novamente as filiais salvas no arquivo JSON.
        """

        # Sem resultado de ping, todas as filiais começam como aguardando.
        if status_por_ip is None:
            status_por_ip = {}

        for item in tabela.get_children():
            tabela.delete(item)

        for filial in carregar_filiais():
            ip = filial["ip"]

            # Busca o status do IP ou usa o estado inicial caso ele não exista.
            status, tag = status_por_ip.get(
                ip,
                ("● Aguardando", "aguardando")
            )

            tabela.insert(
                "",
                "end",
                values=(status, filial["nome"], ip),
                tags=(tag,)
            )

    def finalizar_atualizacao(status_por_ip):
        """
        Atualiza a tabela e libera o início de uma nova verificação.
        """
        nonlocal monitoramento_em_andamento

        atualizar_tabela(status_por_ip)
        ultima_atualizacao_var.set(
            f"Última atualização: {datetime.now().strftime('%H:%M:%S')}"
        )
        monitoramento_em_andamento = False

    def verificar_status_em_segundo_plano():
        """
        Executa o ping das filiais sem bloquear a interface.
        """
        status_por_ip = {}

        # Verifica o roteador de cada filial e guarda o resultado pelo endereço IP.
        for filial in carregar_filiais():
            ip = filial["ip"]

            if testar_ping(ip):
                status_por_ip[ip] = ("● Online", "online")
            else:
                status_por_ip[ip] = ("● Indisponível", "indisponivel")

        # Solicita à janela principal que atualize a tabela com os resultados.
        janela.after(0, finalizar_atualizacao, status_por_ip)

    def atualizar_status():
        """
        Inicia a verificação de ping em uma thread separada.
        """
        nonlocal monitoramento_em_andamento

        # Impede que uma nova verificação comece antes da atual terminar.
        if monitoramento_em_andamento:
            return

        monitoramento_em_andamento = True

        Thread(
            target=verificar_status_em_segundo_plano,
            daemon=True
        ).start()

    def executar_monitoramento_automatico():
        """
        Executa a atualização e agenda uma nova verificação.
        """
        atualizar_status()

        janela.after(
            INTERVALO_ATUALIZACAO,
            executar_monitoramento_automatico
        )

    def cadastrar_filial():
        """
        Salva a filial informada e atualiza a lista da interface.
        """
        if adicionar_filial(nome_var.get(), ip_var.get()):
            nome_var.set("")
            ip_var.set("")
            atualizar_tabela()
            campo_nome.focus()
        else:
            messagebox.showwarning(
                "Cadastro não realizado",
                "Informe uma filial e um IP válidos ou utilize um nome diferente."
            )

    def preparar_edicao_filial():
        """
        Carrega nos campos os dados da filial selecionada na tabela.
        """
        nonlocal filial_em_edicao

        itens_selecionados = tabela.selection()

        if not itens_selecionados:
            messagebox.showwarning(
                "Nenhuma filial selecionada",
                "Selecione uma filial na tabela antes de editar."
            )
            return

        item = itens_selecionados[0]
        valores = tabela.item(item, "values")

        filial_em_edicao = valores[1]
        nome_var.set(valores[1])
        ip_var.set(valores[2])
        campo_nome.focus()

    def salvar_edicao_filial():
        """
        Salva as alterações realizadas na filial selecionada.
        """
        nonlocal filial_em_edicao

        if filial_em_edicao is None:
            messagebox.showwarning(
                "Nenhuma edição iniciada",
                "Selecione uma filial e clique em Editar filial."
            )
            return

        if editar_filial(
            filial_em_edicao,
            nome_var.get(),
            ip_var.get()
        ):
            filial_em_edicao = None
            nome_var.set("")
            ip_var.set("")
            atualizar_tabela()
            atualizar_status()
            campo_nome.focus()
        else:
            messagebox.showwarning(
                "Edição não realizada",
                "Informe dados válidos ou utilize um nome diferente."
            )

    def confirmar_formulario():
        """
        Adiciona uma filial ou salva a edição que estiver em andamento.
        """
        if filial_em_edicao is None:
            cadastrar_filial()
        else:
            salvar_edicao_filial()

    def excluir_filial_selecionada():
        """
        Exclui a filial selecionada na tabela após solicitar confirmação.
        """
        nonlocal filial_em_edicao

        itens_selecionados = tabela.selection()

        if not itens_selecionados:
            messagebox.showwarning(
                "Nenhuma filial selecionada",
                "Selecione uma filial na tabela antes de excluir."
            )
            return

        item = itens_selecionados[0]
        valores = tabela.item(item, "values")
        nome_filial = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja realmente excluir a filial {nome_filial}?"
        )

        if not confirmar:
            return

        if excluir_filial(nome_filial):
            filial_em_edicao = None
            nome_var.set("")
            ip_var.set("")
            atualizar_tabela()
            campo_nome.focus()
        else:
            messagebox.showerror(
                "Erro ao excluir",
                "A filial selecionada não foi encontrada."
            )

    botao_adicionar = ttk.Button(
        cadastro,
        text="Adicionar filial",
        style="Adicionar.TButton",
        command=cadastrar_filial
    )
    botao_adicionar.grid(row=1, column=2, sticky="ew")
    botao_atualizar = ttk.Button(
        cadastro,
        text="Atualizar status",
        style="Adicionar.TButton",
        command=atualizar_status
    )
    botao_atualizar.grid(
        row=2,
        column=2,
        sticky="e",
        pady=(12, 0)
    )

    acoes_cadastro = ttk.Frame(
        cadastro,
        style="Cadastro.TFrame"
    )
    acoes_cadastro.grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="w",
        pady=(12, 0)
    )

    botao_excluir = ttk.Button(
        acoes_cadastro,
        text="Excluir filial",
        style="Adicionar.TButton",
        command=excluir_filial_selecionada
    )
    botao_excluir.pack(side="left")

    botao_editar = ttk.Button(
        acoes_cadastro,
        text="Editar filial",
        style="Adicionar.TButton",
        command=preparar_edicao_filial
    )
    botao_editar.pack(
        side="left",
        padx=(10, 0)
    )

    botao_salvar_edicao = ttk.Button(
        acoes_cadastro,
        text="Salvar edição",
        style="Adicionar.TButton",
        command=salvar_edicao_filial
    )
    botao_salvar_edicao.pack(
        side="left",
        padx=(10, 0)
    )

    texto_ultima_atualizacao = ttk.Label(
        conteudo,
        textvariable=ultima_atualizacao_var,
        style="Descricao.TLabel"
    )
    texto_ultima_atualizacao.pack(
        anchor="e",
        pady=(0, 5)
    )

    # Permite adicionar uma filial ou salvar uma edição pressionando Enter.
    janela.bind("<Return>", lambda evento: confirmar_formulario())

    tabela.pack(fill="both", expand=True)

    atualizar_tabela()
    executar_monitoramento_automatico()
    campo_nome.focus()

    janela.mainloop()


if __name__ == "__main__":
    iniciar_interface()