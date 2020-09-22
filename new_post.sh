#!/bin/bash
if [[ $# != 1 ]]; then echo "$0 <article-slug>"; exit 1; fi

cd ./content/drafts/

article_slug=$1
article_file=${article_slug}.md
# replace - with _ for the filename
article_file=$(echo ${article_file} | tr - _)
touch ${article_file}

echo "Title: " > ${article_file}
echo "Date: $(date +"%Y-%m-%d %H:%M")" >> ${article_file}
echo "Tags:" >> ${article_file}
echo "Author: Raymundo Cassani" >> ${article_file}
echo "Slug: ${article_slug}" >> ${article_file}
echo "Thumbnail: default.png" >> ${article_file}
echo "Created content/drafts/${article_file}"
