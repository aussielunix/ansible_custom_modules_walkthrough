# Custom local Ansible module

This is a demo of a simple, local custom Ansible module.

See if you can work out why this playbook fails.

```bash
lunix@dev: ~/workshop/step1 $ ansible-playbook playbook/emjay.yml -v
```

```bash
lunix@dev: ~/workshop/step1 $ ansible-playbook playbook/emjay.yml -v

Using ~/workshop/step1/ansible.cfg as config file
ERROR! couldn't resolve module/action 'emjay'. This often indicates a misspelling, missing collection, or incorrect module path.

The error appears to be in '~/workshop/step1/playbook/emjay.yml': line 7, column 7, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  tasks:
    - name: testing emjay module
      ^ here

lunix@dev: ~/workshop/step1 $ 
```

