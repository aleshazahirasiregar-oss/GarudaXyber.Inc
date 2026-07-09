import tkinter as tk
from tkinter import messagebox
import time
import os
import sys

# =====================================================================
# STAGE 1: GARUDA XYBER INC - BOOTLOADER ANIMATION (KODE KE-DUA)
# =====================================================================
def run_bootloader():
    # Bersihkan layar terminal sebelum booting
    os.system('cls' if os.name == 'nt' else 'clear')
    print("====================================================")
    print("      GARUDA XYBER INC - WINDOS90 BOOTLOADER v0.90  ")
    print("         NT 3+MS Dos terakhir - Version 3.0.00.     ")
    print("====================================================")
    time.sleep(1)
    print("\n[*] Decompressing Windos90 Kernel...")
    time.sleep(1.2)
    print("[*] Mounting MS-DOS Legacy Emulation Structure...")
    time.sleep(0.8)
    print("[*] Loading Network Profiles (GarudaTunnel & FireDNS)...")
    time.sleep(1)
    print("[V] System Core Initialized Successfully.")
    print("[!] Mengalihkan kontrol ke Antarmuka Grafis (GUI)...")
    print("====================================================")
    time.sleep(1.5)

# Jalankan animasi bootloader terlebih dahulu di terminal
run_bootloader()


# =====================================================================
# STAGE 2: WINDOS90 RETRO DESKTOP INTERACTION (KODE KE-SATU)
# =====================================================================
class Windows90App:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 90 - Retro Python Edition")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Menggunakan font monospace tebal biar jadul
        self.font_main = ("Courier New", 10, "bold")
        self.font_title = ("Courier New", 11, "bold")
        
        # Warna Hijau Tua Khas Desktop 90an
        self.bg_color = "#008080" 
        self.root.configure(bg=self.bg_color)
        
        self.create_desktop()
        self.create_taskbar()
        self.create_start_menu()
        self.create_windows()
        
        self.update_clock()

    def create_desktop(self):
        # Area Ikon Desktop
        # Icon MICI.EXE
        self.icon_mici = tk.Frame(self.root, bg=self.bg_color, cursor="hand2")
        self.icon_mici.place(x=30, y=30, width=100, height=90)
        self.icon_mici.bind("<Button-1>", lambda e: self.open_app("mici"))
        
        lbl_pic1 = tk.Label(self.icon_mici, text="📦", font=("Courier New", 24), bg=self.bg_color, fg="white")
        lbl_pic1.pack()
        lbl_txt1 = tk.Label(self.icon_mici, text="MICI.EXE", font=self.font_main, bg=self.bg_color, fg="white")
        lbl_txt1.pack()

        # Icon DOS_CMD.EXE
        self.icon_dos = tk.Frame(self.root, bg=self.bg_color, cursor="hand2")
        self.icon_dos.place(x=30, y=140, width=100, height=90)
        self.icon_dos.bind("<Button-1>", lambda e: self.open_app("terminal"))
        
        lbl_pic2 = tk.Label(self.icon_dos, text="📟", font=("Courier New", 24), bg=self.bg_color, fg="white")
        lbl_pic2.pack()
        lbl_txt2 = tk.Label(self.icon_dos, text="DOS_CMD.EXE", font=self.font_main, bg=self.bg_color, fg="white")
        lbl_txt2.pack()

    def create_taskbar(self):
        # Gray Taskbar tebal di bawah ala Win95/90
        self.taskbar = tk.Frame(self.root, bg="#c0c0c0", bd=2, relief="raised", height=45)
        self.taskbar.pack(side="bottom", fill="x")
        
        # Tombol Start Tengah ala Modifikasi Windows 11
        self.start_btn = tk.Button(self.taskbar, text="❖ Start", font=self.font_main, bg="#000080", fg="white", 
                                   relief="raised", bd=2, command=self.toggle_start_menu)
        self.start_btn.place(relx=0.4, rely=0.5, anchor="center", width=80, height=30)
        
        self.btn_mici_tb = tk.Button(self.taskbar, text="📦 MICI", font=self.font_main, bg="#c0c0c0", fg="black",
                                     relief="raised", bd=2, command=lambda: self.open_app("mici"))
        self.btn_mici_tb.place(relx=0.48, rely=0.5, anchor="center", width=70, height=30)
        
        self.btn_dos_tb = tk.Button(self.taskbar, text="📟 DOS", font=self.font_main, bg="#c0c0c0", fg="black",
                                    relief="raised", bd=2, command=lambda: self.open_app("terminal"))
        self.btn_dos_tb.place(relx=0.56, rely=0.5, anchor="center", width=70, height=30)

        # Jam Retro di Pojok Kanan
        self.clock_lbl = tk.Label(self.taskbar, text="00:00 AM", font=self.font_main, bg="#c0c0c0", 
                                  fg="black", bd=2, relief="sunken", width=12)
        self.clock_lbl.pack(side="right", padx=10, pady=5)

    def create_start_menu(self):
        self.start_menu = tk.Frame(self.root, bg="#c0c0c0", bd=2, relief="raised", width=250, height=180)
        self.start_menu_visible = False
        
        # Sidebar Start Menu
        sidebar = tk.Label(self.start_menu, text="WINDOWS 90", bg="#808080", fg="white", font=self.font_title, width=22)
        sidebar.pack(side="top", fill="x", pady=2)
        
        # Opsi Pilihan
        opt_mici = tk.Button(self.start_menu, text="📂 MICI Engine", font=self.font_main, bg="#c0c0c0", fg="black", 
                             anchor="w", bd=0, activebackground="#000080", activeforeground="white", command=lambda: self.open_app("mici"))
        opt_mici.pack(fill="x", padx=5, pady=2)
        
        opt_dos = tk.Button(self.start_menu, text="📟 MS-DOS Prompt", font=self.font_main, bg="#c0c0c0", fg="black", 
                            anchor="w", bd=0, activebackground="#000080", activeforeground="white", command=lambda: self.open_app("terminal"))
        opt_dos.pack(fill="x", padx=5, pady=2)
        
        opt_shutdown = tk.Button(self.start_menu, text="🔌 Shutdown OS", font=self.font_main, bg="#c0c0c0", fg="black", 
                                 anchor="w", bd=0, activebackground="#000080", activeforeground="white", command=self.shutdown)
        opt_shutdown.pack(fill="x", padx=5, pady=2)

    def toggle_start_menu(self):
        if self.start_menu_visible:
            self.start_menu.place_forget()
            self.start_menu_visible = False
        else:
            # Letakkan tepat di tengah atas tombol start
            self.start_menu.place(x=275, y=370)
            self.start_menu.lift()
            self.start_menu_visible = True

    def create_windows(self):
        # 1. Jendela Jendela MICI Control
        self.win_mici = tk.Frame(self.root, bg="#c0c0c0", bd=3, relief="raised")
        self.setup_window_header(self.win_mici, "MICI_CONTROL.EXE", "mici")
        
        body_mici = tk.Frame(self.win_mici, bg="white", bd=2, relief="sunken")
        body_mici.pack(fill="both", expand=True, padx=4, pady=4)
        
        txt_mici = (
            "== MICI Core Setup 1990 ==\n\n"
            "Sistem Keamanan Windows 90 Ultra-Protected\n"
            "versi 1.90 aktif penuh.\n\n"
            "BASE MEMORY : 640 KB OK\n"
            "EXT. MEMORY  : 1024 KB OK\n"
            "TUNNEL DRIVER: CARRIER DETECTED [🟢]\n\n"
            "Status: Jaringan Jenderal aman terpantau."
        )
        lbl_mici = tk.Label(body_mici, text=txt_mici, font=self.font_main, bg="white", fg="black", justify="left", anchor="nw")
        lbl_mici.pack(fill="both", expand=True, padx=10, pady=10)

        # 2. Jendela DOS Prompt Interaktif (Bisa Mengetik)
        self.win_terminal = tk.Frame(self.root, bg="#c0c0c0", bd=3, relief="raised")
        self.setup_window_header(self.win_terminal, "MS-DOS Prompt v5.00", "terminal")
        
        self.body_dos = tk.Frame(self.win_terminal, bg="black", bd=2, relief="sunken")
        self.body_dos.pack(fill="both", expand=True, padx=4, pady=4)
        
        self.dos_log = tk.Text(self.body_dos, bg="black", fg="white", font=self.font_main, bd=0, state="normal", height=15)
        self.dos_log.pack(fill="both", expand=True, padx=5, pady=5)
        self.dos_log.insert("end", "GarudaXyber MS-DOS Emulator ver 1.11-1990\n(C)Copyright GarudaXyber Corp 1990.\n\nKetik 'help' untuk daftar perintah retro.\n\nC:\\XYBER> ")
        self.dos_log.config(state="disabled")
        
        # Garis Input CMD
        input_frame = tk.Frame(self.body_dos, bg="black")
        input_frame.pack(fill="x", padx=5, pady=2)
        
        lbl_prompt = tk.Label(input_frame, text="C:\\XYBER> ", font=self.font_main, bg="black", fg="white")
        lbl_prompt.pack(side="left")
        
        self.cmd_input = tk.Entry(input_frame, bg="black", fg="white", font=self.font_main, bd=0, insertbackground="white")
        self.cmd_input.pack(side="left", fill="x", expand=True)
        self.cmd_input.bind("<Return>", self.execute_dos_command)

    def setup_window_header(self, window_frame, title_text, app_id):
        header = tk.Frame(window_frame, bg="#000080", height=25)
        header.pack(fill="x")
        
        lbl_title = tk.Label(header, text=title_text, font=self.font_main, bg="#000080", fg="white")
        lbl_title.pack(side="left", padx=5)
        
        btn_close = tk.Button(header, text="X", font=("Courier New", 8, "bold"), bg="#c0c0c0", fg="black",
                              relief="raised", bd=1, command=lambda: self.close_app(app_id))
        btn_close.pack(side="right", padx=2, pady=2)
        
        # Mekanik Drag & Drop Jendela
        header.bind("<Button-1>", lambda e: self.start_drag(e, window_frame))
        header.bind("<B1-Motion>", lambda e: self.drag_window(e, window_frame))

    def start_drag(self, event, window_frame):
        window_frame.lift()
        window_frame.x = event.x
        window_frame.y = event.y

    def drag_window(self, event, window_frame):
        deltax = event.x - window_frame.x
        deltay = event.y - window_frame.y
        x = window_frame.winfo_x() + deltax
        y = window_frame.winfo_y() + deltay
        window_frame.place(x=x, y=y)

    def open_app(self, app_id):
        if self.start_menu_visible:
            self.toggle_start_menu()
            
        if app_id == "mici":
            self.win_mici.place(x=150, y=80, width=500, height=350)
            self.win_mici.lift()
        elif app_id == "terminal":
            self.win_terminal.place(x=180, y=120, width=520, height=380)
            self.win_terminal.lift()
            self.cmd_input.focus_set()

    def close_app(self, app_id):
        if app_id == "mici":
            self.win_mici.place_forget()
        elif app_id == "terminal":
            self.win_terminal.place_forget()

    def execute_dos_command(self, event):
        command = self.cmd_input.get().strip()
        if not command:
            return
            
        response = ""
        if command.lower() == "help":
            response = "Perintah yang tersedia:\n  help   - Info bantuan\n  ver     - Cek versi sistem operasi\n  cls     - Bersihkan layar\n  dir     - Lihat isi folder root"
        elif command.lower() == "ver":
            response = "GarudaXyber Windows 90 Desktop [Version 1.11.1990]"
        elif command.lower() == "dir":
            response = " Volume in drive C has no label.\n Directory of C:\\XYBER\n\nMICI      EXE         1,024 KB\nDOS_CMD  EXE            512 KB\n3 File(s)       1,536 KB free"
        elif command.lower() == "cls":
            self.dos_log.config(state="normal")
            self.dos_log.delete("1.0", "end")
            self.dos_log.insert("end", "C:\\XYBER> ")
            self.dos_log.config(state="disabled")
            self.cmd_input.delete(0, "end")
            return
        else:
            response = f"Bad command or file name: '{command}'"
            
        self.dos_log.config(state="normal")
        self.dos_log.insert("end", f"{command}\n{response}\n\nC:\\XYBER> ")
        self.dos_log.config(state="disabled")
        self.dos_log.see("end")
        self.cmd_input.delete(0, "end")

    def update_clock(self):
        current_time = time.strftime("%I:%M %p")
        self.clock_lbl.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def shutdown(self):
        messagebox.showinfo("Shutdown", "Shutdown Berhasil. Aman untuk mematikan komputer Anda.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = Windows90App(root)
    root.mainloop()