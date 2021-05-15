"""
Code last update 15.05.2021
This is example use of yclients library.
"""

from yclients import YClientsAPI
import pandas as pd

if __name__ == '__main__':
    TOKEN = "your_token"
    СID = 'your_company_id'
    FID = 'form id'

    # Your yclients autorisation information
    login = "example@gmail.com"
    password = "password"

    # Create api object
    api = YClientsAPI(token=TOKEN, company_id=СID, form_id=FID)

    # Show debugging process
    api.show_debugging()

    # Get user token from the system
    # You can save this token (like bearer token)
    #   and there is no need to update it every time
    user_token = api.get_user_token(login, password)

    # Update autorisation parameters of the api class with user token
    api.update_user_token(user_token)

    # Shows user permissions
    api.show_user_permissions()

    # Get clients list
    clients_data_list = api.get_clients_data()

    # parse clients data
    df = api.parse_clients_data(clients_data_list)
    # show id, name and number of visits for all clients
    print(df[['id', 'name', 'visits']])

    # clients ids list
    all_clients_ids = list(df['id'])

    # show all visits for client with cid
    cid = 20419758
    client_visits = api.get_visits_for_client(cid)
    print(f'Client {cid} visits')
    print(f'{pd.DataFrame(client_visits)}')

    # show all visits for all clients
    all_clients_visits = api.get_visits_data_for_clients_list(all_clients_ids)
    for cid in all_clients_visits.keys():
        print(f'Client {cid} visits')
        print(f'{pd.DataFrame(all_clients_visits[cid])}')

    # show all attended visits for client with cid
    cid = 20419758
    client_visits = api.get_attended_visits_for_client(cid)
    print(f'Client {cid} attended visits')
    print(f'{pd.DataFrame(client_visits)}')

    # show attended visits information for clients:
    df = api.get_attended_visits_dates_information(all_clients_ids)
    print(f'Attended visits dataframe: {df}')

    # show attended visits information for clients with at least one visit:
    print(f"Attended visits ndataframe with no gaps {df[df['visits_number']>0]}")