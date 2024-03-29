import wx
from gui_base import GUIBase

class GUI(GUIBase):
	def __init__(self, options,
			encrypt_file,
			decrypt_archive,
			find_files
		):
		self.app = wx.App()
		super().__init__(None)
		self._set_gui(options)

		self.options = options
		self.decrypt_archive = decrypt_archive
		self.encrypt_file = encrypt_file
		self.find_files = find_files
		self.file_list_folder = {}
		self.file_list_file = {}

		
	def _set_gui(self, options):
		self.file_list.AppendColumn("Path", 240)
		self.file_list.AppendColumn("State", 160)
		if options.encrypt_path:
			self.encrypt_path_text.SetLabel(options.encrypt_path)
		if options.export_path:
			self.export_path_text.SetLabel(options.export_path)	

	def set_file_list(self, files:list):
		self.file_list.DeleteAllItems()
		root = self.file_list.GetRootItem()
		self.file_list_folder = {
			"": root
		}
		self.file_list_file = {}

		def create_folder(path:str):
			(folder, _, name) = path.rpartition("/")
			
			if(folder in self.file_list_folder):
				child = self.file_list.AppendItem(self.file_list_folder[folder], name)
				self.file_list.SetItemData(child, path)
				self.file_list_folder[path] = child
			else:
				create_folder(folder)
				create_folder(path)

		for file in files:
			(path, _, name) = file["file_path"].rpartition("/")
			if(path not in self.file_list_folder):
				create_folder(path)
			child = self.file_list.AppendItem(self.file_list_folder[path], name)
			self.file_list.SetItemText(child, 1, file["state"])
			self.file_list.SetItemData(child, file)
			self.file_list_file[file["file_path"]] = child

	def set_file_list_item_state(self, file_path, state):
		item = self.file_list_file[file_path]
		self.file_list.SetItemText(item, 1, state)

	# override
	def file_listOnTreelistSelectionChanged( self, event ):
		select = self.file_list.Selection
		if(select):
			data = self.file_list.GetItemData(select)
			if(type(data) == dict):
				self.e_encrypt_btn.Enable(True)
				self.e_decrypt_btn.Enable(True)
			else:
				self.e_encrypt_btn.Enable(False)
				self.e_decrypt_btn.Enable(False)
		else:
			self.e_encrypt_btn.Enable(False)
			self.e_decrypt_btn.Enable(False)

	def e_encrypt_btnOnButtonClick(self, event):
		select = self.file_list.Selection
		data = self.file_list.GetItemData(select)
		self.encrypt_file(data)
	
	def e_decrypt_btnOnButtonClick(self, event):
		select = self.file_list.Selection
		data = self.file_list.GetItemData(select)
		if(not data):
			return
		self.decrypt_archive(data)


	def ep_encrypt_browse_btnOnButtonClick(self, event):
		with wx.DirDialog(self, "Open", style=wx.DD_DIR_MUST_EXIST) as dirDialog:
			if dirDialog.ShowModal() == wx.ID_CANCEL:
				return
			dir = dirDialog.GetPath()
		self.options.encrypt_path = dir
		self.encrypt_path_text.SetLabel(self.options.encrypt_path)
		self.find_files()
		
	def ep_export_browse_btnOnButtonClick(self, event):
		with wx.DirDialog(self, "Open", style=wx.DD_DIR_MUST_EXIST) as dirDialog:
			if dirDialog.ShowModal() == wx.ID_CANCEL:
				return
			dir = dirDialog.GetPath()
		self.options.export_path = dir
		self.export_path_text.SetLabel(self.options.export_path)



	def run(self):
		self.Show()
		self.app.MainLoop()




