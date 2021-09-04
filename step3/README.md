# Custom local Ansible module with local module_utils

This is a demo of a simple, local custom Ansible module that relies on local module_utils.

It fails. Can you see why ?.

```bash
lunix@dev: ~/workshop/step3 $ ansible-playbook playbook/emjay.yml -vv
```

```bash
lunix@dev: ~/workshop/step3 $ ansible-playbook playbook/emjay.yml -v

Using ~/workshop/step3/ansible.cfg as config file

PLAY [testing modules] ************************************************************************************************************************************************************************

TASK [testing emjay module] *******************************************************************************************************************************************************************
fatal: [127.0.0.1]: FAILED! => {"msg": "Could not find imported module support code for ansible.modules.emjay.  Looked for (['ansible.module_utils.lunix.test_function', 'ansible.module_utils.lunix'])"}

PLAY RECAP ************************************************************************************************************************************************************************************
127.0.0.1                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0

lunix@dev: ~/workshop/step3 $

```

