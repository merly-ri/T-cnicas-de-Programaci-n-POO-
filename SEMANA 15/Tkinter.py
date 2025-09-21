import tkinter as tk
from tkinter import ttk, messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")
        self.root.geometry("650x400")

        # Lista de eventos
        frame_lista = ttk.Frame(self.root, padding="10")
        frame_lista.pack(fill="both", expand=True)

        columnas = ("Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(frame_lista, columns=columnas, show="headings", height=10)
        self.tree.pack(side="left", fill="both", expand=True)

        for col in columnas:
            self.tree.heading(col, text=col)

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Entrada de datos
        frame_entrada = ttk.Frame(self.root, padding="10")
        frame_entrada.pack(fill="x")

        ttk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.fecha_entry = ttk.Entry(frame_entrada)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.hora_entry = ttk.Entry(frame_entrada)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.desc_entry = ttk.Entry(frame_entrada, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Botones
        frame_botones = ttk.Frame(self.root, padding="10")
        frame_botones.pack(fill="x")

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=10)
        ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side="left", padx=10)
        ttk.Button(frame_botones, text="Salir", command=self.root.quit).pack(side="right", padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get().strip()
        hora = self.hora_entry.get().strip()
        desc = self.desc_entry.get().strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos Vacíos", "Por favor, completa todos los campos.")
            return

        self.tree.insert("", "end", values=(fecha, hora, desc))
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar Evento", "Por favor selecciona un evento para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento seleccionado?"):
            for item in seleccionado:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
