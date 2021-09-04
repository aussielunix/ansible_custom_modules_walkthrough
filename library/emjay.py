#!/usr/bin/env python 

# DOCUMENTATION NORMALLY
# GOES HERE
#

from ansible.module_utils.basic import AnsibleModule

def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        mysetting=dict(required=False,type='str')
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Conveniently bring into current namespace
    mysetting = module.params['mysetting']

    # Seed the result dict()
    result = dict(
        changed=False,
        msg='mysetting: {0}'.format(mysetting)
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # This is how you would test if a 3rd party Python module is installed
    #
    #try:
    #    # Importing the modules here allows us to catch them not being installed on remote hosts
    #    # and pass back a failure via ansible instead of a stack trace.
    #    import pexpect
    #except ImportError:
    #    module.fail_json(msg="You must have the pexpect python module installed to use this Ansible module." 

    # The meat of the actual module
    #
    try:
        # normally a method is called here declared elsewhere
        # that would process the inputs etc and then return some values
        # But we just pretent a python function was called and worked and we
        # set changed = True
        result['changed'] = True
    except:
        module.fail_json(msg="Unable to process input variable into string")
    
    module.exit_json(**result)

if __name__ == '__main__':
    main()
