# 참고 명령어

## Helm 설정 파일 적용

```Bash
helm upgrade prometheus prometheus-community/kube-prometheus-stack -n monitoring -f prom-config.yaml
```

## Prometheus + Grafana 포트 포워딩

- Prometheus

  ```Bash
  kubectl patch svc prometheus-kube-prometheus-prometheus -n monitoring -p '{"spec": {"type": "NodePort", "ports": [{"port": 9090, "nodePort": 30100, "protocol": "TCP", "targetPort": 9090}]}}'
  ```

- Grafana

  ```Bash
  kubectl patch svc prometheus-grafana -n monitoring -p '{"spec": {"ports": [{"port": 80, "targetPort": 3000, "protocol": "TCP", "nodePort": 30090}], "type": "NodePort"}}'
  ```
