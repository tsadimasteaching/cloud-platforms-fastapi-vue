# Ansible


## SSH Forwarding
Before running ansible playbook, run the following commands

```bash
eval $(ssh-agent)
ssh-add ~/.ssh/id_rsa
ssh-add -L
```