company_data = dict()
command = ''
while command != 'End':
    command = input()
    if command == 'End':
        continue

    company_name, employee_id = command.split(' -> ')
    if company_name not in company_data.keys():
        company_data[company_name] = [employee_id]
    else:
        if employee_id not in company_data[company_name]:
            company_data[company_name].append(employee_id)

for company_name, employee_id in company_data.items():
    print(company_name)
    for employee in employee_id:
        print(f"-- {employee}")

