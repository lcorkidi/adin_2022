#!/bin/bash

cwd=$(pwd)
# echo "Entering app directory..."
cd ${APPDIR}

echo "Creating list model info..."
python manage.py list_model_info --field-class > ${DOCSDIR}/list_model_info.txt
echo "list_model_info.txt added to docs"

echo "Creating graphs representations..."
app_labels=('people' 'properties' 'reports' 'accountables' 'accounting' 'references')
python manage.py graph_models -g \
                              -o ${DOCSDIR}/${APPNAME}_models_graph.png \
                              -E \
                              ${app_labels[@]} > ${DOCSDIR}/${APPNAME}_models_graph.dot
echo ".dot and .png files added to docs"

# echo "Leaving app directory"
cd ${cwd} 
