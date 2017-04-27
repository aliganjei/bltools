set +x
for f in $(seq -w 84 150); 
do 
  if [ ! -f "royal/f${f}r.jpg" ]; then
    echo "royal/f${f}r.jpg" doesnt exist
    echo Running: node dezoomify-node.js "http://www.bl.uk/manuscripts/Proxy.ashx?view=io_islamic_3540_f${f}r.xml" "royal/f${f}r.jpg"
    node dezoomify-node.js "http://www.bl.uk/manuscripts/Proxy.ashx?view=io_islamic_3540_f${f}r.xml" "royal/f${f}r.jpg" >> progress.log 2>&1
    echo sleeping
    sleep 300
  else
    echo "royal/f${f}r.jpg" already downloaded
  fi
  if [ ! -f "royal/f${f}v.jpg" ]; then
    echo "royal/f${f}v.jpg" doesnt exist
    echo Running node dezoomify-node.js "http://www.bl.uk/manuscripts/Proxy.ashx?view=io_islamic_3540_f${f}v.xml" "royal/f${f}v.jpg"
    node dezoomify-node.js "http://www.bl.uk/manuscripts/Proxy.ashx?view=io_islamic_3540_f${f}v.xml" "royal/f${f}v.jpg" >> progress.log 2>&1
    echo sleeping
    sleep 300 
  else
    echo "royal/f${f}v.jpg" already downloaded
  fi
done
