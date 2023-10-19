# ProjectBackend

## Problema 1: Anonimização de Metadados de Imagens DICOM

### Descrição do Problema

Os laboratórios que solicitam serviços de dosimetria à Dosimagem precisam anonimizar os metadados das imagens submetidas, em respeito à Lei Geral de Proteção de Dados (LGPD). Isso consome tempo dos responsáveis pelos laboratórios e atrasa o início do trabalho da Dosimagem, pois nem todos os clientes possuem conhecimento para realizar essa tarefa. Portanto, é necessária a criação de uma API REST capaz de receber imagens no formato DICOM e anonimizar seus metadados, incluindo o nome do paciente, sua data de nascimento e outros metadados sensíveis.

### Ferramentas

- [3D Slicer](https://download.slicer.org/)
- [ImageJ](https://imagej.nih.gov/ij/download.html)
- [Pydicom](https://pydicom.github.io/)
- [dcm4che](https://github.com/dcm4che/dcm4che)

## Problema 2: Segmentação de Imagens DICOM

### Descrição do Problema

A Dosimagem utiliza a ferramenta 3D Slicer para realizar a segmentação de órgãos. No 3D Slicer, a ferramenta TotalSegmentatorAI pode realizar a segmentação de forma automática em poucos minutos. O objetivo é desenvolver uma API REST capaz de receber imagens no formato DICOM e segmentá-las automaticamente.

### Ferramentas

- [3D Slicer](https://download.slicer.org/)
- [ImageJ](https://imagej.nih.gov/ij/download.html)

