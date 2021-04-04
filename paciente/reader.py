import pydicom
from datetime import datetime
import glob
import json
from PIL import Image
import matplotlib.pyplot as plt

def get_paciente_info():
    exames = glob.glob("../dicoms/*")
    extensao = "/*000001.dcm"
    paciente_id=[]
    paciente_sexo=[]
    numero_acesso=[]
    data_estudo=[]
    espacamento_slice=[]
    datajson=[]
    for exame in exames:
        resultado = glob.glob(exame+extensao)
        ds = pydicom.dcmread(resultado[0], force=True)
        paciente_id.append(ds.PatientID)
        paciente_sexo.append(ds.PatientSex)
        numero_acesso.append(ds.AccessionNumber)
        data_estudo.append(ds.StudyDate)
        espacamento_slice.append(ds.SliceThickness)
        
    for i in range(len(paciente_id)):
        db= {
            "model":"paciente.Paciente", 
            "pk": i,
            "fields":{"paciente_id":paciente_id[i],"paciente_sexo":paciente_sexo[i],"numero_acesso": numero_acesso[i],"data_estudo":data_estudo[i],"espacamento_slice":espacamento_slice[i]}
        }
        datajson.append(db)
    with open('../data.json', 'w') as f:
        json.dump(datajson, f)


def get_imagem_exame():
    exames = glob.glob("../dicoms/*")
    extensao = "/*000001.dcm"
    pixel_array = []
    for exame in exames:
        resultado = glob.glob(exame+extensao)
        ds = pydicom.dcmread(resultado[0], force=True)
        pixel_array.append(ds.pixel_array)
        plt.imshow(ds.pixel_array,plt.cm.bone)
        plt.savefig('../img/'+ds.PatientID+'.png')
    


get_imagem_exame()