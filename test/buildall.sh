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
sudo echo /home/vagrant/iSDX/examples/test*-mh-bh/config | xargs -n 1 cp /home/vagrant/endeavour/examples/test-mh/config/gauge*
sudo echo /home/vagrant/iSDX/examples/test*-mh-lb/config | xargs -n 1 cp /home/vagrant/endeavour/examples/test-mh/config/gauge*