# Walthrough creating custom Ansible modules

I couldn't quite make sense of the Ansible documentation extend the capability of Ansible.  
What I needed was a guided walkthrough of building a simple module and module_utils.  
This is the guided walthrough I wish I had.  

## Aim of this walkthrough

The aim of this is to demonstrate how the mechanism for loading custom modules and module_utils in Ansible works.  
It starts off small and each step builds on the previous one.  

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a `<Linux/Mac>` working environment
* You have a recent version of Ansible installed
* You have a basic grasp of writing Python and how PYTHONPATH works
* You have an understanding of the Ansible [module architecture](https://docs.ansible.com/ansible-core/devel/dev_guide/developing_program_flow_modules.html) 

## Outline

* [step 1](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step1/) is a playbook with a custom module but it fails to run
* [step 2](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step2/) is a playbook with a custom module and it **works**
* [step 3](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step3/) is a playbook with a custom module that makes use of a python function declared in a `module_util` but it fails to run
* [step 4](https://github.com/aussielunix/ansible_custom_modules_demo/blob/main/step4/) is a playbook with a custom module that makes use of a python function declared in a `module_util` and it **works**

## Links used in researching this

* [Ansible Core Documentation](https://docs.ansible.com/ansible-core/devel/index.html)
* [Ansible Developer Guide](https://docs.ansible.com/ansible-core/devel/dev_guide/index.html)
* [Ansible module architecture](https://docs.ansible.com/ansible-core/devel/dev_guide/developing_program_flow_modules.html)
* [Using and developing module utilities](https://docs.ansible.com/ansible-core/devel/dev_guide/developing_module_utilities.htm)
* [Adding modules and plugins locally](https://docs.ansible.com/ansible/latest/dev_guide/developing_locally.html)
* [Ansible Core module utils](https://github.com/ansible/ansible/tree/devel/lib/ansible/module_utils) examples
* [Ansible search path for modules, plugins etc](https://docs.ansible.com/ansible-core/devel/dev_guide/overview_architecture.html#ansible-search-path)
* [Ansible Configuration Settings](https://docs.ansible.com/ansible-core/devel/reference_appendices/config.html)
* [Example](https://github.com/ansible/ansible/blob/devel/hacking/env-setup) of how to setup your local env. for `module_util` development
* [Debugging modules](https://docs.ansible.com/ansible-core/devel/dev_guide/debugging.html)
* [Developing plugins](https://docs.ansible.com/ansible-core/devel/dev_guide/developing_plugins.html)
* [Developing plugins for network](https://docs.ansible.com/ansible/4/network/dev_guide/developing_plugins_network.html)

## Items yet to be documented

* packaging up custom modules to be installed as an Ansible Collection
* packaging up custom module_utils to be installed via pip
* handling python dependencies within our custom modules
* Documenting custom modules
* Testing custom modules

## Contact

If you want to contact me you can reach me on Twitter - [@twitter](https://twitter.com/aussielunix), [email](mailto:aussielunix@gmail.com) or raise an issue in this repository.

## License

This project is licensed under the MIT [LICENSE](LICENSE)
