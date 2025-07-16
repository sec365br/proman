import os
from datetime import datetime

class Playbook:
    def __init__(self, identification, incident_identification, attack_steps, data_steps, mitigation_steps, containment_steps, conclusion):
        self.identification = identification
        self.incident_identification = incident_identification
        self.attack_steps = attack_steps
        self.data_steps = data_steps
        self.mitigation_steps = mitigation_steps
        self.containment_steps = containment_steps
        self.conclusion = conclusion
    
    def generate_playbook(self):
        """Gera o playbook no formato HTML para exibição no Streamlit"""
        html_content = f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; background-color: #f8f9fa; border-radius: 8px; margin: 10px 0;">
            <h2 style="color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;">
                PLAYBOOK - {self.identification}
            </h2>
            
            <div style="background-color: white; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #e74c3c; margin-top: 0;">IDENTIFICAÇÃO:</h3>
                <p style="text-align: justify; color: #2c3e50; margin: 10px 0;">
                    {self.incident_identification}
                </p>
            </div>
            
            <div style="background-color: white; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #e74c3c; margin-top: 0;">ETAPAS DO ATAQUE:</h3>
                <div style="color: #2c3e50;">
                    {"<br>".join(self.attack_steps)}
                </div>
            </div>
            
            <div style="background-color: white; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #e74c3c; margin-top: 0;">AVALIAÇÃO:</h3>
                <div style="color: #2c3e50;">
                    {"<br>".join(self.data_steps)}
                </div>
            </div>
            
            <div style="background-color: white; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #e74c3c; margin-top: 0;">MITIGAÇÃO:</h3>
                <div style="color: #2c3e50;">
                    {"<br>".join(self.mitigation_steps)}
                </div>
            </div>
            
            <div style="background-color: white; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #e74c3c; margin-top: 0;">CONTENÇÃO:</h3>
                <div style="color: #2c3e50;">
                    {"<br>".join(self.containment_steps)}
                </div>
            </div>
            
            <div style="background-color: white; padding: 15px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h3 style="color: #e74c3c; margin-top: 0;">CONCLUSÃO:</h3>
                <p style="text-align: justify; color: #2c3e50; margin: 10px 0;">
                    {self.conclusion}
                </p>
            </div>
            
            <div style="text-align: center; margin-top: 20px; color: #7f8c8d; font-size: 12px;">
                <p>Playbook gerado em: {datetime.now().strftime("%d/%m/%Y às %H:%M:%S")}</p>
            </div>
        </div>
        """
        return html_content
    
    def generate_txt_file(self, filename=None):
        """Gera um arquivo .txt com o conteúdo do playbook"""
        if filename is None:
            filename = f"playbook_{self.identification}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Conteúdo do arquivo TXT
        txt_content = f"""PLAYBOOK - {self.identification}
{'=' * 50}

IDENTIFICAÇÃO:
{self.incident_identification}

ETAPAS DO ATAQUE:
{chr(10).join(self.attack_steps)}

AVALIAÇÃO:
{chr(10).join(self.data_steps)}

MITIGAÇÃO:
{chr(10).join(self.mitigation_steps)}

CONTENÇÃO:
{chr(10).join(self.containment_steps)}

CONCLUSÃO:
{self.conclusion}

{'=' * 50}
Playbook gerado em: {datetime.now().strftime("%d/%m/%Y às %H:%M:%S")}
"""
        
        # Criar o arquivo
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(txt_content)
            return filename, True, "Arquivo gerado com sucesso!"
        except Exception as e:
            return filename, False, f"Erro ao gerar arquivo: {str(e)}"
    
    def generate_formatted_string(self):
        """Gera uma string formatada similar ao formato dos exemplos fornecidos"""
        formatted_content = f'''"{self.identification}":"<p align=justify><b>IDENTIFICAÇÃO:</b>\\n {self.incident_identification} \\n \\n <b>ETAPAS DO ATAQUE:</b>\\n {" ".join([step.replace("0", "") + "\\n" for step in self.attack_steps])} \\n <b>AVALIAÇÃO:</b>\\n {" ".join([step + "\\n" for step in self.data_steps])} \\n <b>MITIGAÇÃO:</b> \\n {" ".join([step.replace("0", "") + "\\n" for step in self.mitigation_steps])} \\n <b>CONTENÇÃO:</b> \\n {" ".join([step.replace("0", "") + "\\n" for step in self.containment_steps])} \\n <b>CONCLUSÃO:</b> {self.conclusion}</p>",'''
        
        return formatted_content
    
    def export_to_dict_format(self):
        """Exporta o playbook no formato de dicionário similar aos exemplos"""
        return {
            self.identification: f'<p align=justify><b>IDENTIFICAÇÃO:</b>\\n {self.incident_identification} \\n \\n <b>ETAPAS DO ATAQUE:</b>\\n {" ".join([step + "\\n" for step in self.attack_steps])} \\n <b>AVALIAÇÃO:</b>\\n {" ".join([step + "\\n" for step in self.data_steps])} \\n <b>MITIGAÇÃO:</b> \\n {" ".join([step + "\\n" for step in self.mitigation_steps])} \\n <b>CONTENÇÃO:</b> \\n {" ".join([step + "\\n" for step in self.containment_steps])} \\n <b>CONCLUSÃO:</b> {self.conclusion}</p>'
        }