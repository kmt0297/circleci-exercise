#!/bin/bash
for i in {1..30}; do
  (echo > /dev/tcp/localhost/5432) 2>/dev/null && echo "DB up" && exit 0
  echo "Waiting for DB..."; sleep 1
done
echo "DB never came up"; exit 1
