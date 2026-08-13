while True:
    print("main menu")
    print("select option")
    main_menu = """
1 Phone book
2 Messages
3 Chat
4 Call register
5 Tones
6 Settings
7 Call divert
8 Games
9 Calculator
10 Reminder
11 Clock
12 Profiles
13 SIM services
0 Exit
"""
    print(main_menu)
    main_menu_choice = int(input("Enter a number: "))

    match main_menu_choice:
        case 1:
            while True:
                print("Phonebook")
                phonebook_menu = """
1 Search
2 Service Nos
3 Add Name
4 Erase
5 Edit
6 Assign tone
7 Send b'card
8 Options
9 Speed dials
10 Voice tags
99 Back
"""
                print(phonebook_menu)
                phonebook_menu_choice = int(input("Enter number: "))

                match phonebook_menu_choice:
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos")
                    case 3:
                        print("Add Name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign tone")
                    case 7:
                        print("Send b'card")
                    case 8:
                        print("Options")
                    case 9:
                        print("Speed dial")
                    case 10:
                        print("Voice tags")
                    case 99:
                        break
                    case _:
                        print("Invalid option")

        case 2:
            while True:
                print("Message")
                message_menu = """
1 Set1
2 Common
3 Chat
4 Call register
5 Show call duration
6 Show call cost
7 Call cost setting
8 Prepaid credit
99 Back
0 Exit
"""
                print(message_menu)
                print("select option")
                message_choice = int(input("Enter a number: "))

                match message_choice:
                    case 1:
                        while True:
                            print("Set1")
                            set1_main_menu = """
1 Message centre number
2 Message sent as
3 Message validity
99 Back
0 Exit
"""
                            print(set1_main_menu)
                            set1_choice = int(input("select an option: "))

                            match set1_choice:
                                case 1:
                                    print("Message centre number")
                                case 2:
                                    print("Message sent as")
                                case 3:
                                    print("Message validity")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 2:
                        while True:
                            print("Common")
                            common_main_menu = """
1 Delivery report
2 Reply via same centre
3 Character support
99 Back
0 Exit
"""
                            print(common_main_menu)
                            print("Choose your choice from the option above")
                            common_choice = int(input("Enter a number: "))

                            match common_choice:
                                case 1:
                                    print("Delivery report")
                                case 2:
                                    print("Reply via same centre")
                                case 3:
                                    print("Character support")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 3:
                        print("Chat")

                    case 4:
                        while True:
                            print("call register")
                            call_register_main_menu = """
1 Missed call
2 Received call
3 Dialled number
4 Erase recent call list
5 Show call duration
99 Back
0 Exit
"""
                            print(call_register_main_menu)
                            print("select an option")
                            call_register_choice = int(input())

                            match call_register_choice:
                                case 1:
                                    print("Missed call")
                                case 2:
                                    print("Received call")
                                case 3:
                                    print("Dialled number")
                                case 4:
                                    print("Erase recent call")
                                case 5:
                                    print("Show call duration")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 5:
                        while True:
                            print("Show call duration")
                            show_call_duration_main_menu = """
1 Last call duration
2 All call duration
3 Received call duration
4 Dialled call duration
5 Clear timer
99 Back
0 Exit
"""
                            print(show_call_duration_main_menu)
                            print("Enter a number")
                            duration_choice = int(input("select an option: "))

                            match duration_choice:
                                case 1:
                                    print("Last call duration")
                                case 2:
                                    print("All call duration")
                                case 3:
                                    print("Received call duration")
                                case 4:
                                    print("Dialled call duration")
                                case 5:
                                    print("Clear timer")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 6:
                        while True:
                            print("Show call cost")
                            show_call_cost_main_menu = """
1 Last call cost
2 All call cost
3 Clear counter
99 Back
0 Exit
"""
                            print(show_call_cost_main_menu)
                            print("Enter a number")
                            show_call_cost_choice = int(input("select an option: "))

                            match show_call_cost_choice:
                                case 1:
                                    print("Last call cost")
                                case 2:
                                    print("All call cost")
                                case 3:
                                    print("Clear counter")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 7:
                        while True:
                            print("Call cost setting")
                            call_cost_setting = """
1 Call cost limit
2 Show cost in
3 Clear counter
99 Back
0 Exit
"""
                            print(call_cost_setting)
                            print("select an option")
                            call_cost_setting_choice = int(input())

                            match call_cost_setting_choice:
                                case 1:
                                    print("Call cost limit")
                                case 2:
                                    print("Show cost in")
                                case 3:
                                    print("Clear counter")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 8:
                        print("Prepaid credit")

                    case 99:
                        break
                    case 0:
                        exit()
                    case _:
                        print("Invalid option")

        case 3:
            print("Chat")

        case 4:
            while True:
                print("call register")
                call_register_menu = """
1 Missed call
2 Received call
3 Dialled number
4 Erase recent call list
5 Show call duration
6 Show call cost
7 Call cost setting
8 Prepaid credit
99 Back
"""
                print(call_register_menu)
                print("Enter a number")
                call_register_choice = int(input())

                match call_register_choice:
                    case 1:
                        print("Missed call")
                    case 2:
                        print("Received call")
                    case 3:
                        print("Dialled number")
                    case 4:
                        print("Erase recent call list")
                    case 5:
                        print("Show call duration")
                    case 6:
                        print("Show call cost")
                    case 7:
                        print("Call cost setting")
                    case 8:
                        print("Prepaid credit")
                    case 99:
                        break
                    case _:
                        print("Invalid option")

        case 5:
            while True:
                print("Tones")
                tone_main_menu = """
1 Ringtone
2 Ringing volume
3 Incoming call alert
4 Composer
5 Message alert tone
6 Keypad tone
7 Warning and game tone
8 Vibrating alert
9 Screen saver
99 Back
0 Exit
"""
                print(tone_main_menu)
                print("Choose your choice from the option above")
                tone_choice = int(input("select an option: "))

                match tone_choice:
                    case 1:
                        print("Ringtone")
                    case 2:
                        print("Ringing volume")
                    case 3:
                        print("Incoming call alert")
                    case 4:
                        print("Composer")
                    case 5:
                        print("Message alert tone")
                    case 6:
                        print("Keypad tone")
                    case 7:
                        print("Warning and game tone")
                    case 8:
                        print("Vibrating alert")
                    case 9:
                        print("Screen saver")
                    case 99:
                        break
                    case 0:
                        exit()
                    case _:
                        print("Invalid option")

        case 6:
            while True:
                print("Setting")
                setting_main_menu = """
1 Call setting
2 Phone setting
3 Security setting
4 Restore factory setting
99 Back
0 Exit
"""
                print(setting_main_menu)
                setting_choice = int(input("select an option: "))

                match setting_choice:
                    case 1:
                        while True:
                            print("Call setting")
                            call_setting_menu = """
1 Automatic redial
2 Speed dialing
3 Call waiting Option
4 Own number sending
5 Phone line in use
6 Automatic answer
99 Back
0 Exit
"""
                            print(call_setting_menu)
                            call_setting_choice = int(input("select an option: "))

                            match call_setting_choice:
                                case 1:
                                    print("Automatic redial")
                                case 2:
                                    print("Speed dialing")
                                case 3:
                                    print("Call waiting option")
                                case 4:
                                    print("Own number sending")
                                case 5:
                                    print("Phone line in use")
                                case 6:
                                    print("Automatic answer")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 2:
                        while True:
                            phone_setting_menu = """
1 Language
2 Cell info display
3 Welcome note
4 Network selection
5 Light
99 Back
0 Exit
"""
                            print(phone_setting_menu)
                            print("Choose your choice from the option above")
                            phone_setting_choice = int(input())

                            match phone_setting_choice:
                                case 1:
                                    print("Language")
                                case 2:
                                    print("Cell info display")
                                case 3:
                                    print("Welcome note")
                                case 4:
                                    print("Network selection")
                                case 5:
                                    print("Light")
                                case 99:
                                    break
                                case 0:
                                    exit()
                                case _:
                                    print("Invalid option")

                    case 3:
                        while True:
                            print("Security setting")
                            security_setting_menu = """
1 PIN code request
2 Call barring service
3 Fixed dialling
4 Closed user group
5 Phone security
6 Change access code
99 Back
"""
                            print(security_setting_menu)
                            print("Choose your choice from the option above")
                            security_setting_choice = int(input())

                            match security_setting_choice:
                                case 1:
                                    print("PIN code request")
                                case 2:
                                    print("Call barring service")
                                case 3:
                                    print("Fixed dialling")
                                case 4:
                                    print("Closed user group")
                                case 5:
                                    print("Phone security")
                                case 6:
                                    print("Change access code")
                                case 99:
                                    break
                                case _:
                                    print("Invalid option")

                    case 4:
                        print("Restore factory setting")

                    case 99:
                        break
                    case 0:
                        exit()
                    case _:
                        print("Invalid option")

        case 7:
            print("Call divert")

        case 8:
            print("Games")

        case 9:
            print("Calculator")

        case 10:
            print("Reminder")

        case 11:
            while True:
                print("Clock")
                clock_menu = """
1 Alarm clock
2 Clock setting
3 Date setting
4 Stopwatch
5 Countdown timer
6 Auto update of date and time
99 Back
0 Exit
"""
                print(clock_menu)
                print("Enter a number")
                clock_choice = int(input())

                match clock_choice:
                    case 1:
                        print("Alarm clock")
                    case 2:
                        print("Clock setting")
                    case 3:
                        print("Date setting")
                    case 4:
                        print("Stopwatch")
                    case 5:
                        print("Countdown timer")
                    case 6:
                        print("Auto update of date and time")
                    case 99:
                        break
                    case 0:
                        exit()
                    case _:
                        print("Invalid option")

        case 12:
            print("Profiles")

        case 13:
            print("SIM services")

        case 0:
            print("Exiting...")
            break

        case _:
            print("Invalid option")
