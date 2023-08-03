# pdf to word

import groupdocs_conversion_cloud

app_sid =  "api SID"
app_key = "api key"

convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)

try:

# Cargar el archivo desde la fuante al almacenamiento

    filename = 'file name.pdf'
    remote_name = 'file name.pdf'
    output_name = 'file name.docx'
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
