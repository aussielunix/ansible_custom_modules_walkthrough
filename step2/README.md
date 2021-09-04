# Custom local Ansible module

This is a demo of a simple, local custom Ansible module.

It works now because we have told Ansible [where](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step2/ansible.cfg#L5) to find our local, custom module.

```bash
lunix@dev: ~/workshop/step2 $ ansible-playbook playbook/emjay.yml -v
```

```bash
lunix@dev: ~/workshop/step2 $ ansible-playbook playbook/emjay.yml -v

Using ~/workshop/step2/ansible.cfg as config file

PLAY [testing modules] ************************************************************************************************************************************************************************

TASK [testing emjay module] *******************************************************************************************************************************************************************
changed: [127.0.0.1] => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"}, "changed": true, "msg": "mysetting: hello"}

PLAY RECAP ************************************************************************************************************************************************************************************
127.0.0.1                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

lunix@dev: ~/workshop/step2 $
```

