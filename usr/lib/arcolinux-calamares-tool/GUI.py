# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================



def GUI(self, Gtk, GdkPixbuf, fn):

    # ======================================================================
    #                   CONTAINERS
    # ======================================================================

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    # =======================================================
    #                       App Notifications
    # =======================================================

    self.notification_revealer = Gtk.Revealer()
    self.notification_revealer.set_reveal_child(False)

    self.notification_label = Gtk.Label()
    #base_dir = os.path.dirname(os.path.realpath(__file__))
    #pb_panel = GdkPixbuf.Pixbuf().new_from_file(base_dir + '/images/panel.png')
    #panel = Gtk.Image().new_from_pixbuf(pb_panel)

    #overlayFrame = Gtk.Overlay()
    #overlayFrame.add(panel)
    #overlayFrame.add_overlay(self.notification_label)

    #self.notification_revealer.add(overlayFrame)
    #hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox0 = Gtk.Box(self.notification_revealer, True, False, 0)
    # Preferred filesystem
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # Save and Close button
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # Liveuser message
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # ArcoLinux Logo
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # Debugging
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # Genereal messages at bottom 
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # ======================================================================
    #                           LOGO
    # ======================================================================

    img_pb = GdkPixbuf.Pixbuf().new_from_file_at_size(fn.os.path.join(str(fn.Path(__file__).parent), 'images/arcolinux-one-liner.png'), 235, 235)  # noqa
    img = Gtk.Image().new_from_pixbuf(img_pb)
    hbox4.pack_start(img, True, False, 0)

    # ======================================================================
    #                           BOX 0
    # ======================================================================

    lbl0 = Gtk.Label(label="Here comes the message ")
 
    hbox0.pack_start(lbl0, False, False, 0)

    # ======================================================================
    #                           BOX 1
    # ======================================================================

    lbl1 = Gtk.Label(label="Select your preferred filesystem: ")
    self.fileSystem = Gtk.ComboBoxText()
    self.fileSystem.set_size_request(280, 0)

    for i in range(len(fn.fs)):
        self.fileSystem.append_text(fn.fs[i])
    self.fileSystem.set_active(0)

    hbox1.pack_start(lbl1, False, False, 0)
    hbox1.pack_end(self.fileSystem, False, False, 0)

    # ======================================================================
    #                           BOX 2
    # ======================================================================

    lbl2 = Gtk.Label(label="Set Calamares to debug mode: ")
    self.debugswitch = Gtk.Switch()
             
    self.debugswitch.connect("notify::active", fn.on_debugswitch_toggled)

    hbox5.pack_start(lbl2, False, False, 0)
    hbox5.pack_end(self.debugswitch, False, False, 0)    

    # ======================================================================
    #                       BUTTONS
    # ======================================================================
    btnCancel = Gtk.Button(label="Close")
    btnCancel.connect('clicked', self.on_close_clicked)
    btnOK = Gtk.Button(label="Save")
    btnOK.connect('clicked', self.on_save_clicked)

    hbox2.pack_end(btnCancel, False, False, 0)
    hbox2.pack_end(btnOK, False, False, 0)

    # ======================================================================
    #                       LIVEUSER MESSAGE
    # ======================================================================
    lblmessage = Gtk.Label()
    lblmessage.set_justify(Gtk.Justification.CENTER)
    lblmessage.set_line_wrap(True)
    lblmessage.set_markup("<span foreground=\"orange\" size=\"xx-large\">" + fn.liveusermessage + "</span>")  # noqa

    hbox3.pack_start(lblmessage, True, False, 0)

    # ======================================================================
    #                       GENERAL MESSAGES
    # ======================================================================
    lblgeneralmessage = Gtk.Label()
    lblgeneralmessage.set_justify(Gtk.Justification.CENTER)
    lblgeneralmessage.set_line_wrap(True)
    lblgeneralmessage.set_markup(fn.calamaresdebugmessage)  # noqa


    hbox6.pack_start(lblgeneralmessage, True, False, 0)

    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================
    #self.vbox.pack_start(hbox0, False, False, 0)
    self.vbox.pack_start(hbox4, False, False, 0)   # LOGO
    self.vbox.pack_start(hbox1, False, False, 0)    # Preferred filesystem
    self.vbox.pack_start(hbox5, False, False, 0)    # Calamares in Debug
    if not fn.users.strip() == fn.liveuser.strip():
        self.vbox.pack_start(hbox3, True, True, 20) # Message liveuser
        btnCancel.set_sensitive(False)
        btnOK.set_sensitive(False)
        self.fileSystem.set_sensitive(False)
    self.vbox.pack_end(hbox2, False, False, 7)      # Buttons
    #self.vbox.pack_start(hbox6, False, False, 20)  # General messages like saved