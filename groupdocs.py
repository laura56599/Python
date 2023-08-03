# pdf to word

import groupdocs_conversion_cloud

app_sid =  "4eaadf6b-a557-4045-a6b0-d22e9bc51310"
app_key = "9a5e10a7061d95f0daeeb6b5b73a2ac9"

convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

try:

# Cargar el archivo desde la fuante al almacenamiento

    filename = 'SOLICITUD AUTORIZACION CITA MEDICA TE VELEZ CORDERO LAURA 03 AGOSTO 2023 1.pdf'
    remote_name = 'SOLICITUD AUTORIZACION CITA MEDICA TE VELEZ CORDERO LAURA 03 AGOSTO 2023 1.pdf'
    output_name = 'SOLICITUD AUTORIZACION CITA MEDICA TE VELEZ CORDERO LAURA 03 AGOSTO 2023 1.docx'
    strformat = 'docx'
    request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name, filename)
    response_upload = file_api.upload_file(request_upload)
    
# extraer texto del archivo pdf

    settings = groupdocs_conversion_cloud.ConvertSettings()
    settings.file_path = remote_name
    settings.format = strformat
    settings.output_path = output_name
    request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
    response = convert_api.convert_document(request)
    
    print("Document converted succesfully: " + str(response))
    
except groupdocs_conversion_cloud.ApiException as e:
    print("Exception when calling get_supported_conversion_types: {0}". format(e.message))