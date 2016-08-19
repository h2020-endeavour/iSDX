mkdir output
for i in specs/*.spec
do
	echo "####################################" $i "########################################################"
	file=`basename $i .spec`
	rm -rf ../examples/$file
	rm -rf output/$file
	python gen_test.py $i
	mv output/$file ../examples
done
rm -r output/

#workaround for yaml files
sudo cp /home/vagrant/iSDX/test/templates/grafana/* /home/vagrant/iSDX/examples/test2-mh-bh/config
