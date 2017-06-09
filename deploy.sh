wget https://github.com/luizalabs/teresa-cli/releases/download/v0.3.2/teresa-li$

mv ./teresa* teresa

chmod +x ./teresa

./teresa version

./teresa config set-cluster $TERESA_CLUSTER_NAME --server $TERESA_CLUSTER_URL

./teresa config use-cluster $TERESA_CLUSTER_NAME

echo $TERESA_PASSWORD | ./teresa login --user $TERESA_USER

./teresa app list
