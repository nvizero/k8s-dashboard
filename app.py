from flask import Flask, jsonify
from kubernetes import client, config

app = Flask(__name__)

# 加載 Kubernetes 配置
config.load_kube_config()

# 創建一個 API 實例
v1 = client.CoreV1Api()

@app.route('/nodes')
def get_nodes():
    # 獲取集群節點信息
    nodes = v1.list_node()
    nodes_list = []
    for node in nodes.items:
        nodes_list.append(node.metadata.name)
    return jsonify(nodes_list)

@app.route('/ns')
def get_ns():
    # 獲取集群namespace
    ns = v1.list_namespace()
    ns_list = []
    for node in ns.items:
        ns_list.append(node.metadata.name)
    return jsonify(ns_list)

if __name__ == '__main__':
    app.run(debug=True)

