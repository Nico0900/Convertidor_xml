import pandas as pd
import json
import csv
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import platform
from i18n import get_i18n

class XMLConverterApp:
    def __init__(self, root):
        self.root = root

        # Inicializar sistema de i18n
        self.i18n = get_i18n()

        self.root.title(self.i18n.get('app_title'))
        self.root.geometry("600x800")
        self.root.resizable(True, True)
        self.root.minsize(650, 550)

        # Variables
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar(value="variables_illustrator.xml")
        self.var_name = tk.StringVar(value="NOMBRE2")
        self.binding_name = tk.StringVar(value="binding1")
        self.selected_column = tk.StringVar()

        # Detectar sistema operativo
        self.os_platform = platform.system()  # 'Darwin' para macOS, 'Windows', 'Linux'

        self.setup_ui()
        
    def setup_ui(self):
        # Título principal
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill="x")

        title_label = ttk.Label(title_frame, text=self.i18n.get('app_title').split(' - ')[0],
                               font=("Arial", 16, "bold"))
        title_label.pack()

        subtitle_label = ttk.Label(title_frame, text=self.i18n.get('app_subtitle'),
                                  font=("Arial", 10))
        subtitle_label.pack()
        
        # Marco principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Sección de archivos soportados
        support_frame = ttk.LabelFrame(main_frame, text=self.i18n.get('supported_formats'), padding="10")
        support_frame.pack(fill="x", pady=(0, 15))

        support_label = ttk.Label(support_frame, text=self.i18n.get('formats_text'),
                                 font=("Consolas", 9), justify="left")
        support_label.pack(anchor="w")
        
        # Selección de archivo
        file_frame = ttk.LabelFrame(main_frame, text=self.i18n.get('select_file'), padding="10")
        file_frame.pack(fill="x", pady=(0, 15))

        file_path_frame = ttk.Frame(file_frame)
        file_path_frame.pack(fill="x")

        ttk.Label(file_path_frame, text=self.i18n.get('file_label')).pack(side="left")
        file_entry = ttk.Entry(file_path_frame, textvariable=self.input_file, width=50)
        file_entry.pack(side="left", padx=(10, 10), fill="x", expand=True)

        browse_btn = ttk.Button(file_path_frame, text=self.i18n.get('browse'),
                               command=self.browse_file, width=10)
        browse_btn.pack(side="right")
        
        # Marco de configuración
        config_frame = ttk.LabelFrame(main_frame, text=self.i18n.get('configuration'), padding="10")
        config_frame.pack(fill="x", pady=(0, 15))

        # Selección de columna
        col_frame = ttk.Frame(config_frame)
        col_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(col_frame, text=self.i18n.get('data_column'), width=15).pack(side="left")
        self.column_combo = ttk.Combobox(col_frame, textvariable=self.selected_column,
                                        state="readonly", width=30)
        self.column_combo.pack(side="left", padx=(10, 0))

        auto_btn = ttk.Button(col_frame, text=self.i18n.get('auto_detect'),
                             command=self.auto_detect_column, width=12)
        auto_btn.pack(side="right")
        
        # Configuración XML
        xml_config_frame = ttk.Frame(config_frame)
        xml_config_frame.pack(fill="x", pady=(10, 0))

        # Variable name
        var_frame = ttk.Frame(xml_config_frame)
        var_frame.pack(fill="x", pady=(0, 5))
        ttk.Label(var_frame, text=self.i18n.get('xml_variable'), width=15).pack(side="left")
        ttk.Entry(var_frame, textvariable=self.var_name, width=20).pack(side="left", padx=(10, 0))

        # Binding name
        binding_frame = ttk.Frame(xml_config_frame)
        binding_frame.pack(fill="x", pady=(0, 5))
        ttk.Label(binding_frame, text=self.i18n.get('binding_name'), width=15).pack(side="left")
        ttk.Entry(binding_frame, textvariable=self.binding_name, width=20).pack(side="left", padx=(10, 0))

        # Archivo de salida
        output_frame = ttk.Frame(config_frame)
        output_frame.pack(fill="x", pady=(10, 0))

        ttk.Label(output_frame, text=self.i18n.get('xml_file'), width=15).pack(side="left")
        ttk.Entry(output_frame, textvariable=self.output_file, width=40).pack(side="left", padx=(10, 10), fill="x", expand=True)
        
        # Estado de generación
        self.status_label = ttk.Label(config_frame, text="", font=("Arial", 10, "bold"))
        self.status_label.pack(pady=(10, 0))
        
        # Botones principales
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(15, 10))

        convert_btn = ttk.Button(button_frame, text=self.i18n.get('generate_xml'),
                                command=self.convert_file,
                                style="Accent.TButton", width=25)
        convert_btn.pack(side="left", padx=(0, 10))

        preview_btn = ttk.Button(button_frame, text=self.i18n.get('preview'),
                               command=self.preview_data, width=15)
        preview_btn.pack(side="left", padx=(0, 10))

        validate_btn = ttk.Button(button_frame, text=self.i18n.get('validate'),
                                 command=self.validate_xml, width=15)
        validate_btn.pack(side="left")

        # Botón para abrir carpeta
        open_folder_btn = ttk.Button(button_frame, text=self.i18n.get('open_folder'),
                                    command=self.open_output_folder, width=15)
        open_folder_btn.pack(side="right")
        
        # Área de log más compacta
        log_frame = ttk.LabelFrame(main_frame, text=self.i18n.get('status_messages'), padding="5")
        log_frame.pack(fill="both", expand=True, pady=(10, 0))

        # Crear el área de texto con scrollbar
        text_frame = ttk.Frame(log_frame)
        text_frame.pack(fill="both", expand=True)

        self.log_text = tk.Text(text_frame, height=6, font=("Consolas", 9),
                               wrap="word", state="disabled")
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)

        self.log_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Log inicial
        self.log(self.i18n.get('app_started'))
        self.log(self.i18n.get('select_file_start'))
    
    def update_status(self, message, color="black"):
        """Actualizar el estado visual"""
        self.status_label.config(text=message, foreground=color)
        self.root.update()
    
    def open_output_folder(self):
        """Abrir la carpeta donde se guarda el XML (compatible con Windows/macOS/Linux)"""
        output_path = self.output_file.get()
        if output_path:
            folder_path = os.path.dirname(os.path.abspath(output_path))
            if os.path.exists(folder_path):
                try:
                    if self.os_platform == "Windows":
                        os.startfile(folder_path)
                    elif self.os_platform == "Darwin":  # macOS
                        import subprocess
                        subprocess.run(["open", folder_path], check=True)
                    else:  # Linux y otros
                        import subprocess
                        subprocess.run(["xdg-open", folder_path], check=True)
                    self.log(self.i18n.get('folder_opened', path=folder_path))
                except Exception as e:
                    messagebox.showerror(self.i18n.get('error'),
                                       f"Error opening folder: {str(e)}")
            else:
                messagebox.showwarning(self.i18n.get('warning'),
                                     self.i18n.get('folder_not_exist'))
        else:
            messagebox.showwarning(self.i18n.get('warning'),
                                 self.i18n.get('no_output_file'))
    
    def log(self, message):
        """Agregar mensaje al log"""
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")
        self.root.update()
    
    def browse_file(self):
        """Abrir diálogo para seleccionar archivo"""
        filetypes = [
            ("Todos los soportados", "*.xlsx;*.xls;*.csv;*.txt;*.json;*.tsv;*.raw;*.data"),
            ("Excel", "*.xlsx;*.xls"),
            ("CSV", "*.csv"),
            ("Texto", "*.txt"),
            ("JSON", "*.json"),
            ("TSV", "*.tsv"),
            ("RAW/Data", "*.raw;*.data"),
            ("Todos los archivos", "*.*")
        ]
        
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de datos",
            filetypes=filetypes
        )
        
        if filename:
            self.input_file.set(filename)
            self.log(self.i18n.get('file_selected', filename=os.path.basename(filename)))
            self.analyze_file()
    
    def analyze_file(self):
        """Analizar el archivo seleccionado"""
        file_path = self.input_file.get()
        if not file_path:
            return

        try:
            self.log(self.i18n.get('analyzing_file'))
            data = self.load_file_data(file_path)

            if isinstance(data, pd.DataFrame):
                columns = list(data.columns)
                self.column_combo['values'] = columns
                self.log(self.i18n.get('columns_found', count=len(columns)))
                self.log(self.i18n.get('data_rows', count=len(data)))

                # Auto-detectar mejor columna
                self.auto_detect_column()
            else:
                self.log(self.i18n.get('analysis_error'))

        except Exception as e:
            self.log(self.i18n.get('error_analyzing', error=str(e)))
    
    def load_file_data(self, file_path):
        """Cargar datos según el tipo de archivo"""
        file_ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if file_ext in ['.xlsx', '.xls']:
                return pd.read_excel(file_path)
            
            elif file_ext == '.csv':
                # Intentar diferentes delimitadores
                for delimiter in [',', ';', '\t']:
                    try:
                        df = pd.read_csv(file_path, delimiter=delimiter)
                        if len(df.columns) > 1:
                            return df
                    except:
                        continue
                # Si falla, usar pandas por defecto
                return pd.read_csv(file_path)
            
            elif file_ext == '.tsv':
                return pd.read_csv(file_path, delimiter='\t')
            
            elif file_ext == '.json':
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # Convertir JSON a DataFrame
                if isinstance(json_data, list):
                    # Si es una lista de objetos
                    if json_data and isinstance(json_data[0], dict):
                        return pd.DataFrame(json_data)
                    else:
                        # Lista simple
                        return pd.DataFrame({'data': json_data})
                elif isinstance(json_data, dict):
                    # Si es un objeto, buscar arrays
                    for key, value in json_data.items():
                        if isinstance(value, list):
                            return pd.DataFrame({key: value})
                    # Si no hay arrays, convertir a DataFrame
                    return pd.DataFrame([json_data])
            
            elif file_ext in ['.txt', '.raw', '.data']:
                # Leer como líneas de texto
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                return pd.DataFrame({'data': lines})
            
            else:
                raise ValueError(self.i18n.get('unsupported_format', ext=file_ext))

        except Exception as e:
            raise Exception(self.i18n.get('file_load_error', error=str(e)))
    
    def auto_detect_column(self):
        """Auto-detectar la mejor columna para datos"""
        file_path = self.input_file.get()
        if not file_path:
            return
            
        try:
            data = self.load_file_data(file_path)
            
            if not isinstance(data, pd.DataFrame):
                return
            
            best_column = None
            max_text_score = 0
            
            for col in data.columns:
                sample_data = data[col].dropna().head(20)
                if len(sample_data) == 0:
                    continue
                
                # Calcular score de texto
                text_count = sum(isinstance(val, str) and len(str(val).strip()) > 0 
                               for val in sample_data)
                text_score = text_count / len(sample_data)
                
                # Penalizar columnas con muchos números
                numeric_count = sum(str(val).replace('.', '').replace('-', '').isdigit() 
                                  for val in sample_data)
                if numeric_count > len(sample_data) * 0.8:
                    text_score *= 0.3
                
                if text_score > max_text_score:
                    max_text_score = text_score
                    best_column = col
            
            if best_column:
                self.selected_column.set(best_column)
                self.log(self.i18n.get('auto_detected', column=best_column, score=max_text_score))

        except Exception as e:
            self.log(self.i18n.get('auto_detect_error', error=str(e)))
    
    def preview_data(self):
        """Mostrar vista previa de los datos"""
        try:
            file_path = self.input_file.get()
            column = self.selected_column.get()

            if not file_path or not column:
                messagebox.showwarning(self.i18n.get('warning'),
                                     self.i18n.get('select_file_column'))
                return

            data = self.load_file_data(file_path)
            values = data[column].dropna().head(10).tolist()

            preview_text = self.i18n.get('preview_header')
            for i, value in enumerate(values, 1):
                preview_text += f"{i:2d}. {str(value)[:50]}{'...' if len(str(value)) > 50 else ''}\n"

            if len(data[column].dropna()) > 10:
                preview_text += self.i18n.get('preview_more', count=len(data[column].dropna()) - 10)

            messagebox.showinfo(self.i18n.get('preview_title'), preview_text)

        except Exception as e:
            messagebox.showerror(self.i18n.get('error'),
                               self.i18n.get('preview_error', error=str(e)))
    
    def convert_file(self):
        """Convertir archivo a XML con la arquitectura exacta de Adobe Illustrator"""
        try:
            # Validar inputs
            file_path = self.input_file.get()
            column = self.selected_column.get()
            output_path = self.output_file.get()
            var_name = self.var_name.get()
            binding_name = self.binding_name.get()

            if not all([file_path, column, output_path, var_name, binding_name]):
                messagebox.showwarning(self.i18n.get('warning'),
                                     self.i18n.get('complete_all_fields'))
                return

            self.log(self.i18n.get('starting_conversion'))
            self.update_status(self.i18n.get('generating_xml'), "blue")

            # Cargar datos
            data = self.load_file_data(file_path)
            values = data[column].dropna().tolist()

            self.log(self.i18n.get('processing_elements', count=len(values)))

            # Generar XML con la arquitectura exacta del archivo muestra
            xml_content = self.generate_adobe_xml(values, var_name, binding_name)

            # Guardar archivo
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(xml_content)

            self.log(self.i18n.get('conversion_complete'))
            self.log(self.i18n.get('file_saved', path=output_path))
            self.log(self.i18n.get('datasets_created', count=len(values)))
            self.update_status(self.i18n.get('xml_generated', count=len(values)), "green")

            # Validar automáticamente
            self.validate_xml()

            # Mensaje de confirmación más visible
            result = messagebox.askyesno(self.i18n.get('success'),
                                       self.i18n.get('success_message',
                                                    filename=os.path.basename(output_path),
                                                    count=len(values),
                                                    location=os.path.dirname(os.path.abspath(output_path))))

            if result:
                self.open_output_folder()

        except Exception as e:
            self.log(self.i18n.get('conversion_error', error=str(e)))
            self.update_status(self.i18n.get('xml_generation_error'), "red")
            messagebox.showerror(self.i18n.get('error'),
                               self.i18n.get('conversion_error', error=str(e)))
    
    def generate_adobe_xml(self, values, var_name, binding_name):
        """Generar XML con la arquitectura exacta de Adobe Illustrator"""
        
        # Escapar caracteres especiales para XML
        def escape_xml(text):
            text = str(text).strip()
            replacements = {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&apos;'
            }
            for char, escape in replacements.items():
                text = text.replace(char, escape)
            return text
        
        # Construir XML línea por línea con la estructura exacta
        xml_lines = []
        
        # Declaración XML y DTD (igual que en el archivo muestra)
        xml_lines.append('<?xml version="1.0" encoding="utf-8"?>')
        xml_lines.append('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN"    "http://www.w3.org/TR/2000/CR-SVG-20001102/DTD/svg-20001102.dtd" [')
        xml_lines.append('\t<!ENTITY ns_graphs "http://ns.adobe.com/Graphs/1.0/">')
        xml_lines.append('\t<!ENTITY ns_vars "http://ns.adobe.com/Variables/1.0/">')
        xml_lines.append('\t<!ENTITY ns_imrep "http://ns.adobe.com/ImageReplacement/1.0/">')
        xml_lines.append('\t<!ENTITY ns_custom "http://ns.adobe.com/GenericCustomNamespace/1.0/">')
        xml_lines.append('\t<!ENTITY ns_flows "http://ns.adobe.com/Flows/1.0/">')
        xml_lines.append('<!ENTITY ns_extend "http://ns.adobe.com/Extensibility/1.0/">')
        xml_lines.append(']>')
        
        # Estructura SVG
        xml_lines.append('<svg>')
        xml_lines.append('<variableSets  xmlns="&ns_vars;">')
        xml_lines.append('')
        xml_lines.append(f'<variableSet locked="none" varSetName="{binding_name}">')
        xml_lines.append('')
        xml_lines.append('<variables>')
        xml_lines.append('')
        xml_lines.append(f'\t<variable varName="{var_name}" trait="textcontent" category="&ns_flows;"></variable>')
        xml_lines.append('')
        xml_lines.append('</variables>')
        xml_lines.append('')
        xml_lines.append('<v:sampleDataSets  xmlns:v="&ns_vars;" xmlns="&ns_custom;">')
        
        # Generar datasets
        for i, value in enumerate(values):
            escaped_value = escape_xml(value)
            
            if i == 0:
                dataset_name = "Data Set"
            else:
                dataset_name = f"Data Set {i}"
            
            xml_lines.append(f'<v:sampleDataSet dataSetName="{dataset_name}">')
            xml_lines.append('')
            xml_lines.append(f'<{var_name}>')
            xml_lines.append(f'\t<p>{escaped_value}</p>')
            xml_lines.append(f'</{var_name}>')
            xml_lines.append('')
            xml_lines.append('</v:sampleDataSet>')
            xml_lines.append('')
        
        # Cerrar estructura
        xml_lines.append('</v:sampleDataSets></variableSet></variableSets></svg>')
        
        return '\n'.join(xml_lines)
    
    def validate_xml(self):
        """Validar el archivo XML generado"""
        output_path = self.output_file.get()

        if not os.path.exists(output_path):
            messagebox.showwarning(self.i18n.get('warning'),
                                 self.i18n.get('no_xml_validate'))
            return

        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                xml_content = f.read()

            # Validación básica - intentar parsear el XML
            from xml.parsers.expat import ParserCreate

            def start_element(name, attrs):
                pass
            def end_element(name):
                pass
            def char_data(data):
                pass

            parser = ParserCreate()
            parser.StartElementHandler = start_element
            parser.EndElementHandler = end_element
            parser.CharacterDataHandler = char_data

            parser.Parse(xml_content, True)

            self.log(self.i18n.get('xml_validated'))
            messagebox.showinfo(self.i18n.get('validate'), self.i18n.get('xml_valid'))

        except Exception as e:
            self.log(self.i18n.get('xml_validation_error', error=str(e)))
            messagebox.showerror(self.i18n.get('error'),
                               self.i18n.get('xml_invalid', error=str(e)))

def main():
    # Crear ventana principal
    root = tk.Tk()
    
    # Configurar estilo
    try:
        root.tk.call('source', 'azure.tcl')
        root.tk.call('set_theme', 'light')
    except:
        pass  # Si no tiene el tema azure, usar el estilo por defecto
    
    # Crear aplicación
    app = XMLConverterApp(root)
    
    # Ejecutar
    root.mainloop()

if __name__ == "__main__":
    main()