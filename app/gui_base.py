import wx
import wx.xrc
import wx.dataview

class GUIBase ( wx.Frame ):
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_main = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.page_encrypt = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_en = wx.BoxSizer( wx.VERTICAL )

		self.file_list = wx.dataview.TreeListCtrl( self.page_encrypt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )

		bSizer_en.Add( self.file_list, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer_en_btns = wx.BoxSizer( wx.HORIZONTAL )


		bSizer_en_btns.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.e_decrypt_btn = wx.Button( self.page_encrypt, wx.ID_ANY, u"decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.e_decrypt_btn.Enable( False )

		bSizer_en_btns.Add( self.e_decrypt_btn, 0, wx.ALL, 5 )

		self.e_encrypt_btn = wx.Button( self.page_encrypt, wx.ID_ANY, u"encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.e_encrypt_btn.Enable( False )

		bSizer_en_btns.Add( self.e_encrypt_btn, 0, wx.ALL, 5 )


		bSizer_en.Add( bSizer_en_btns, 0, wx.EXPAND, 5 )


		self.page_encrypt.SetSizer( bSizer_en )
		self.page_encrypt.Layout()
		bSizer_en.Fit( self.page_encrypt )
		self.m_notebook.AddPage( self.page_encrypt, u"files", True )
		self.page_options = wx.Panel( self.m_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_opt = wx.BoxSizer( wx.VERTICAL )

		bSizer_encrypt_path = wx.BoxSizer( wx.HORIZONTAL )

		self.m_ep_text = wx.StaticText( self.page_options, wx.ID_ANY, u"Encrypt Path:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_ep_text.Wrap( -1 )

		bSizer_encrypt_path.Add( self.m_ep_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.encrypt_path_text = wx.StaticText( self.page_options, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.encrypt_path_text.Wrap( -1 )

		bSizer_encrypt_path.Add( self.encrypt_path_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ep_encrypt_browse_btn = wx.Button( self.page_options, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_encrypt_path.Add( self.ep_encrypt_browse_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer_opt.Add( bSizer_encrypt_path, 0, wx.EXPAND, 5 )

		bSizer_export_path = wx.BoxSizer( wx.HORIZONTAL )

		self.m_ep2_text = wx.StaticText( self.page_options, wx.ID_ANY, u"Export Path:", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_ep2_text.Wrap( -1 )

		bSizer_export_path.Add( self.m_ep2_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.export_path_text = wx.StaticText( self.page_options, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.export_path_text.Wrap( -1 )

		bSizer_export_path.Add( self.export_path_text, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ep_export_browse_btn = wx.Button( self.page_options, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_export_path.Add( self.ep_export_browse_btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer_opt.Add( bSizer_export_path, 0, wx.EXPAND, 5 )


		self.page_options.SetSizer( bSizer_opt )
		self.page_options.Layout()
		bSizer_opt.Fit( self.page_options )
		self.m_notebook.AddPage( self.page_options, u"options", False )

		bSizer_main.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer_main )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.file_list.Bind( wx.dataview.EVT_TREELIST_SELECTION_CHANGED, self.file_listOnTreelistSelectionChanged )
		self.e_decrypt_btn.Bind( wx.EVT_BUTTON, self.e_decrypt_btnOnButtonClick )
		self.e_encrypt_btn.Bind( wx.EVT_BUTTON, self.e_encrypt_btnOnButtonClick )
		self.ep_encrypt_browse_btn.Bind( wx.EVT_BUTTON, self.ep_encrypt_browse_btnOnButtonClick )
		self.ep_export_browse_btn.Bind( wx.EVT_BUTTON, self.ep_export_browse_btnOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def file_listOnTreelistSelectionChanged( self, event ):
		event.Skip()

	def e_decrypt_btnOnButtonClick( self, event ):
		event.Skip()

	def e_encrypt_btnOnButtonClick( self, event ):
		event.Skip()

	def ep_encrypt_browse_btnOnButtonClick( self, event ):
		event.Skip()

	def ep_export_browse_btnOnButtonClick( self, event ):
		event.Skip()

