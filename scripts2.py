import pandas as pd
import json
import csv
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys

class XMLConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor Universal a XML - Adobe Illustrator")
        self.root.geometry("600x800")
        self.root.resizable(True, True)
        self.root.minsize(650, 550)
        
        # Variables
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar(value="variables_illustrator.xml")
        self.var_name = tk.StringVar(value="NOMBRE2")
        self.binding_name = tk.StringVar(value="binding1")
        self.selected_column = tk.StringVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Título principal
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill="x")
        
        title_label = ttk.Label(title_frame, text="Convertidor Universal a XML", 
                               font=("Arial", 16, "bold"))
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, text="Para Variables de Adobe Illustrator", 
                                  font=("Arial", 10))
        subtitle_label.pack()
        
        # Marco principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Sección de archivos soportados
        support_frame = ttk.LabelFrame(main_frame, text="Formatos Soportados", padding="10")
        support_frame.pack(fill="x", pady=(0, 15))
        
        support_text = """📁 Formatos de archivo compatibles:
• Excel (.xlsx, .xls) - Hojas de cálculo
• CSV (.csv) - Valores separados por comas
• TXT (.txt) - Archivos de texto plano (línea por línea)
• JSON (.json) - Archivos JSON con arrays o objetos
• TSV (.tsv) - Valores separados por tabulaciones
• RAW (.raw, .data) - Datos en texto plano"""
        
        support_label = ttk.Label(support_frame, text=support_text, 
                                 font=("Consolas", 9), justify="left")
        support_label.pack(anchor="w")
        
        # Selección de archivo
        file_frame = ttk.LabelFrame(main_frame, text="Seleccionar Archivo", padding="10")
        file_frame.pack(fill="x", pady=(0, 15))
        
        file_path_frame = ttk.Frame(file_frame)
        file_path_frame.pack(fill="x")
        
        ttk.Label(file_path_frame, text="Archivo:").pack(side="left")
        file_entry = ttk.Entry(file_path_frame, textvariable=self.input_file, width=50)
        file_entry.pack(side="left", padx=(10, 10), fill="x", expand=True)
        
        browse_btn = ttk.Button(file_path_frame, text="Buscar", 
                               command=self.browse_file, width=10)
        browse_btn.pack(side="right")
        
        # Marco de configuración
        config_frame = ttk.LabelFrame(main_frame, text="Configuración", padding="10")
        config_frame.pack(fill="x", pady=(0, 15))
        
        # Selección de columna
        col_frame = ttk.Frame(config_frame)
        col_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(col_frame, text="Columna de datos:", width=15).pack(side="left")
        self.column_combo = ttk.Combobox(col_frame, textvariable=self.selected_column, 
                                        state="readonly", width=30)
        self.column_combo.pack(side="left", padx=(10, 0))
        
        auto_btn = ttk.Button(col_frame, text="Auto-detectar", 
                             command=self.auto_detect_column, width=12)
        auto_btn.pack(side="right")
        
        # Configuración XML
        xml_config_frame = ttk.Frame(config_frame)
        xml_config_frame.pack(fill="x", pady=(10, 0))
        
        # Variable name
        var_frame = ttk.Frame(xml_config_frame)
        var_frame.pack(fill="x", pady=(0, 5))
        ttk.Label(var_frame, text="Variable XML:", width=15).pack(side="left")
        ttk.Entry(var_frame, textvariable=self.var_name, width=20).pack(side="left", padx=(10, 0))
        
        # Binding name
        binding_frame = ttk.Frame(xml_config_frame)
        binding_frame.pack(fill="x", pady=(0, 5))
        ttk.Label(binding_frame, text="Binding name:", width=15).pack(side="left")
        ttk.Entry(binding_frame, textvariable=self.binding_name, width=20).pack(side="left", padx=(10, 0))
        
        # Archivo de salida
        output_frame = ttk.Frame(config_frame)
        output_frame.pack(fill="x", pady=(10, 0))
        
        ttk.Label(output_frame, text="Archivo XML:", width=15).pack(side="left")
        ttk.Entry(output_frame, textvariable=self.output_file, width=40).pack(side="left", padx=(10, 10), fill="x", expand=True)
        
        # Estado de generación
        self.status_label = ttk.Label(config_frame, text="", font=("Arial", 10, "bold"))
        self.status_label.pack(pady=(10, 0))
        
        # Botones principales
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(15, 10))
        
        convert_btn = ttk.Button(button_frame, text="📄 GENERAR ARCHIVO XML", 
                                command=self.convert_file, 
                                style="Accent.TButton", width=25)
        convert_btn.pack(side="left", padx=(0, 10))
        
        preview_btn = ttk.Button(button_frame, text="👁 Vista Previa", 
                               command=self.preview_data, width=15)
        preview_btn.pack(side="left", padx=(0, 10))
        
        validate_btn = ttk.Button(button_frame, text="✓ Validar XML", 
                                 command=self.validate_xml, width=15)
        validate_btn.pack(side="left")
        
        # Botón para abrir carpeta
        open_folder_btn = ttk.Button(button_frame, text="📁 Abrir Carpeta", 
                                    command=self.open_output_folder, width=15)
        open_folder_btn.pack(side="right")
        
        # Área de log más compacta
        log_frame = ttk.LabelFrame(main_frame, text="Estado y Mensajes", padding="5")
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
        self.log("🚀 Convertidor Universal XML iniciado")
        self.log("📝 Selecciona un archivo para comenzar")
    
    def update_status(self, message, color="black"):
        """Actualizar el estado visual"""
        self.status_label.config(text=message, foreground=color)
        self.root.update()
    
    def open_output_folder(self):
        """Abrir la carpeta donde se guarda el XML"""
        output_path = self.output_file.get()
        if output_path:
            folder_path = os.path.dirname(os.path.abspath(output_path))
            if os.path.exists(folder_path):
                if sys.platform == "win32":
                    os.startfile(folder_path)
                elif sys.platform == "darwin":
                    os.system(f"open '{folder_path}'")
                else:
                    os.system(f"xdg-open '{folder_path}'")
                self.log(f"📁 Carpeta abierta: {folder_path}")
            else:
                messagebox.showwarning("Advertencia", "La carpeta no existe")
        else:
            messagebox.showwarning("Advertencia", "No hay archivo de salida especificado")
    
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
            self.log(f"📁 Archivo seleccionado: {os.path.basename(filename)}")
            self.analyze_file()
    
    def analyze_file(self):
        """Analizar el archivo seleccionado"""
        file_path = self.input_file.get()
        if not file_path:
            return
            
        try:
            self.log("🔍 Analizando archivo...")
            data = self.load_file_data(file_path)
            
            if isinstance(data, pd.DataFrame):
                columns = list(data.columns)
                self.column_combo['values'] = columns
                self.log(f"📊 Columnas encontradas: {len(columns)}")
                self.log(f"📝 Filas de datos: {len(data)}")
                
                # Auto-detectar mejor columna
                self.auto_detect_column()
            else:
                self.log("❌ No se pudo analizar la estructura del archivo")
                
        except Exception as e:
            self.log(f"❌ Error al analizar: {str(e)}")
    
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
                raise ValueError(f"Formato de archivo no soportado: {file_ext}")
                
        except Exception as e:
            raise Exception(f"Error cargando archivo: {str(e)}")
    
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
                self.log(f"🎯 Auto-detectado: '{best_column}' ({max_text_score:.1%} contenido textual)")
            
        except Exception as e:
            self.log(f"❌ Error en auto-detección: {str(e)}")
    
    def preview_data(self):
        """Mostrar vista previa de los datos"""
        try:
            file_path = self.input_file.get()
            column = self.selected_column.get()
            
            if not file_path or not column:
                messagebox.showwarning("Advertencia", "Selecciona archivo y columna primero")
                return
            
            data = self.load_file_data(file_path)
            values = data[column].dropna().head(10).tolist()
            
            preview_text = "Vista previa (primeros 10 elementos):\n\n"
            for i, value in enumerate(values, 1):
                preview_text += f"{i:2d}. {str(value)[:50]}{'...' if len(str(value)) > 50 else ''}\n"
            
            if len(data[column].dropna()) > 10:
                preview_text += f"\n... y {len(data[column].dropna()) - 10} elementos más"
            
            messagebox.showinfo("Vista Previa", preview_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en vista previa: {str(e)}")
    
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
                messagebox.showwarning("Advertencia", "Completa todos los campos")
                return
            
            self.log("🔄 Iniciando conversión...")
            self.update_status("🔄 Generando archivo XML...", "blue")
            
            # Cargar datos
            data = self.load_file_data(file_path)
            values = data[column].dropna().tolist()
            
            self.log(f"📊 Procesando {len(values)} elementos")
            
            # Generar XML con la arquitectura exacta del archivo muestra
            xml_content = self.generate_adobe_xml(values, var_name, binding_name)
            
            # Guardar archivo
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(xml_content)
            
            self.log("✅ ¡Conversión completada!")
            self.log(f"💾 Archivo guardado: {output_path}")
            self.log(f"📈 Datasets creados: {len(values)}")
            self.update_status(f"✅ ¡XML GENERADO EXITOSAMENTE! ({len(values)} elementos)", "green")
            
            # Validar automáticamente
            self.validate_xml()
            
            # Mensaje de confirmación más visible
            result = messagebox.askyesno("¡Éxito!", 
                                       f"¡Archivo XML generado correctamente!\n\n"
                                       f"📁 Archivo: {os.path.basename(output_path)}\n"
                                       f"📊 Elementos: {len(values)}\n"
                                       f"📍 Ubicación: {os.path.dirname(os.path.abspath(output_path))}\n\n"
                                       f"¿Deseas abrir la carpeta donde se guardó?")
            
            if result:
                self.open_output_folder()
                
        except Exception as e:
            self.log(f"❌ Error en conversión: {str(e)}")
            self.update_status("❌ Error al generar XML", "red")
            messagebox.showerror("Error", f"Error en la conversión:\n{str(e)}")
    
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
            messagebox.showwarning("Advertencia", "No hay archivo XML para validar")
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
            
            self.log("✅ XML validado correctamente")
            messagebox.showinfo("Validación", "✅ El archivo XML es válido para Adobe Illustrator")
            
        except Exception as e:
            self.log(f"❌ Error de validación XML: {e}")
            messagebox.showerror("Error de Validación", f"XML inválido:\n{str(e)}")

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