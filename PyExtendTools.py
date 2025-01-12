# -*- coding: utf-8 -*-

import ast
import concurrent.futures
import datetime
import json
import locale
from mutagen.easyid3 import EasyID3
import mutagen.id3
import mutagen.flac
import mutagen.mp3
import mutagen.mp4
import numpy
import os
import pathlib
import py7zr
import platform
import re
import shutil
import send2trash
import sys
import tarfile
import time
import threading
import psutil
import zipfile
import pyqtgraph
from PySide6.QtCore import (QCoreApplication, QByteArray, QMetaObject, QRect, Qt, Signal, QSize, QFile, QEvent, QFileInfo, QTimer, QLocale, QThread)
from PySide6.QtGui import (QFont, QStandardItem, QStandardItemModel, QDesktopServices, QCursor, QPixmap, QIcon, QImage, QGuiApplication, QColor)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QListView, QLineEdit, QMainWindow, QPlainTextEdit, QPushButton, QTabWidget, QTreeView, QWidget, QFileSystemModel, QMenu, QAbstractItemView, QDialog, QDialogButtonBox, QFileIconProvider, QGridLayout, QScrollArea, QCalendarWidget)
from PySide6.QtCharts import (QChart, QChartView, QPieSeries, QPieSlice)

BackupNowPath = [u'']
PathListory = [u'']
SelectedItemPath = [u'']
CopiedItems = [u'']
CopiedItemCount = [0]
SortedNumbar = [u'']
SelectedItem = [u'0']
QLinePath = [u'']
PathHistorys = []
PathHistorys2 = [u'']
CheckPaths = [u'0']
StopPath = [u'0']
StopPath2 = [u'0']
NowRootDirectoryPath = [u'']
BackupRootPath = [os.path.expanduser(u'~')]
OneChecked = [u'1']
OneChecked2 = [u'0']
OneChecked3 = [u'0']
BackPageIndex = [1]
EditFilePath = []
EditMediaPath_FLAC = []
EditMediaPath_M4A = []
EditMediaPath_MP3 = []
DropedCoverImage = [u'']
DropedCheck = [u'0']

try:
	locale.setlocale(locale.LC_CTYPE, u'Japanese_Japan.932')
except:
	locale.setlocale(locale.LC_TIME, u'ja_JP.UTF-8')
LoadThread = concurrent.futures.ThreadPoolExecutor(os.cpu_count() * 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 * 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
OutOfThread0 = QThread()

class SystemInfoWidget(QWidget):
	def __init__(self, parent=None):
		super(SystemInfoWidget, self).__init__(parent)
		self.cpu = QLabel()
		self.cpu.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.cpu.setMinimumWidth(350)
		self.cpuLabel = QLabel()
		self.cpuLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.cpuLabel.setText('CPU使用率: ')
		self.cpuLabel.setAlignment(Qt.AlignLeft)
		self.diskExplainLabel = QLabel()
		self.diskExplainLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.diskExplainLabel.setText('ディスク使用容量 / 空き容量: ')
		self.diskFree = QLabel()
		self.diskFree.setMinimumWidth(350)
		self.diskFree.setAlignment(Qt.AlignLeft)
		self.diskFree.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.diskUsed = QLabel()
		self.diskUsed.setMinimumWidth(350)
		self.diskUsed.setAlignment(Qt.AlignLeft)
		self.diskUsed.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.diskUsedCapacity = QLabel()
		self.diskUsedCapacity.setMinimumWidth(350)
		self.diskUsedCapacity.setAlignment(Qt.AlignLeft)
		self.diskUsedCapacity.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.diskUsedCapacityLabel = QLabel()
		self.diskUsedCapacityLabel.setAlignment(Qt.AlignLeft)
		self.diskUsedCapacityLabel.setMinimumWidth(160)
		self.diskUsedCapacityLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.diskUsedCapacityLabel.setText('ディスク使用量: ')
		self.diskUsedCapacityLabel.setAlignment(Qt.AlignLeft)
		self.diskframe = QLabel()
		self.diskframe.setAlignment(Qt.AlignCenter)
		self.diskframe.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.diskframe.setMaximumHeight(1)
		self.diskframe.setMinimumWidth(600)
		self.frame0 = QLabel()
		self.frame0.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.frame0.setMaximumHeight(1)
		self.frame0.setMinimumWidth(550)
		self.frame1 = QLabel()
		self.frame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.frame1.setMaximumHeight(1)
		self.frame1.setMinimumWidth(550)
		self.frame2 = QLabel()
		self.frame2.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.frame2.setMaximumHeight(1)
		self.frame2.setMinimumWidth(550)
		self.frame3 = QLabel()
		self.frame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.frame3.setMaximumHeight(1)
		self.frame3.setMinimumWidth(550)
		self.frame4 = QLabel()
		self.frame4.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.frame4.setMaximumHeight(1)
		self.frame4.setMinimumWidth(550)
		self.memoryExplainLabel = QLabel()
		self.memoryExplainLabel.setAlignment(Qt.AlignLeft)
		self.memoryExplainLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.memoryExplainLabel.setText('メモリー使用率 / 空き容量: ')
		self.memoryExplainLabel.setMinimumWidth(160)
		self.memoryFree = QLabel()
		self.memoryFree.setAlignment(Qt.AlignLeft)
		self.memoryFree.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.memoryFree.setMinimumWidth(350)
		self.memoryUsed = QLabel()
		self.memoryUsed.setAlignment(Qt.AlignLeft)
		self.memoryUsed.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.memoryUsed.setMinimumWidth(350)
		self.memoryUsedCapacityPercent = QLabel()
		self.memoryUsedCapacityPercent.setMinimumWidth(350)
		self.memoryUsedCapacityPercent.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.memoryUsedCapacityPercentLabel = QLabel()
		self.memoryUsedCapacityPercentLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.memoryUsedCapacityPercentLabel.setAlignment(Qt.AlignLeft)
		self.memoryUsedCapacityPercentLabel.setText('物理メモリー使用率: ')
		self.network = QLabel()
		self.network.setAlignment(Qt.AlignLeft)
		self.network.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.network.setMinimumWidth(350)
		self.networkLabel = QLabel()
		self.networkLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.networkLabel.setText('ネットワーク使用率: ')
		self.networkLabel.setAlignment(Qt.AlignLeft)
		self.virtualMemoryFree = QLabel()
		self.virtualMemoryFree.setAlignment(Qt.AlignLeft)
		self.virtualMemoryFree.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.virtualMemoryFree.setMinimumWidth(450)
		self.virtualMemoryUsed = QLabel()
		self.virtualMemoryUsed.setMinimumWidth(450)
		self.virtualMemoryUsed.setAlignment(Qt.AlignLeft)
		self.virtualMemoryUsed.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.virtualMemoryUsedCapacity = QLabel()
		self.virtualMemoryUsedCapacity.setMinimumWidth(350)
		self.virtualMemoryUsedCapacity.setAlignment(Qt.AlignLeft)
		self.virtualMemoryUsedCapacity.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.virtualMemoryUsedCapacityLabel = QLabel()
		self.virtualMemoryUsedCapacityLabel.setAlignment(Qt.AlignLeft)
		self.virtualMemoryUsedCapacityLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.virtualMemoryUsedCapacityLabel.setText('仮想メモリー使用率: ')
		self.virtualmemoryExplainLabel = QLabel()
		self.virtualmemoryExplainLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.virtualmemoryExplainLabel.setText('仮想メモリー使用量 / 空き容量: ')
		threading.Thread(target=self.CPUMontor, daemon=True).start()
		threading.Thread(target=self.MemoryMonitor, daemon=True).start()
		threading.Thread(target=self.WiFiSpeedRate, daemon=True).start()
		threading.Thread(target=self.UsedMemory, daemon=True).start()
		threading.Thread(target=self.FreeMemory, daemon=True).start()
		threading.Thread(target=self.SwapMemoryUsedPercent, daemon=True).start()
		threading.Thread(target=self.SwapUsed, daemon=True).start()
		threading.Thread(target=self.SwapFree, daemon=True).start()
		threading.Thread(target=self.DiskUsedPercent, daemon=True).start()
		threading.Thread(target=self.DiskUsed, daemon=True).start()
		threading.Thread(target=self.DiskFree, daemon=True).start()
		self.SystemInfoLayout = QGridLayout()
		self.SystemInfoLayout.addWidget(self.frame0, 0, 0)
		self.SystemInfoLayout.addWidget(self.networkLabel, 1, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.network, 1, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.frame1, 2, 0)
		self.SystemInfoLayout.addWidget(self.cpuLabel, 3, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.cpu, 3, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.frame2, 4, 0)
		self.SystemInfoLayout.addWidget(self.memoryUsedCapacityPercentLabel, 5, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.memoryUsedCapacityPercent, 5, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.memoryUsed, 6, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.memoryExplainLabel, 7, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.memoryFree, 8, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.frame3, 9, 0)
		self.SystemInfoLayout.addWidget(self.virtualMemoryUsedCapacityLabel, 10, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.virtualMemoryUsedCapacity, 10, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.virtualMemoryUsed, 11, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.virtualmemoryExplainLabel, 12, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.virtualMemoryFree, 13, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.frame4, 14, 0)
		self.SystemInfoLayout.addWidget(self.diskUsedCapacityLabel, 15, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.diskUsedCapacity, 15, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.diskFree, 16, 1, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.diskExplainLabel, 17, 0, Qt.AlignCenter)
		self.SystemInfoLayout.addWidget(self.diskUsed, 18, 1, Qt.AlignCenter)
		for Col in range(self.SystemInfoLayout.columnCount()):
			self.SystemInfoLayout.setColumnMinimumWidth(Col, 5000)
		self.SystemInfoLayout.setContentsMargins(10, 0, 0, 0)
		self.setLayout(self.SystemInfoLayout)
		self.setMinimumWidth(600)
		self.setMaximumWidth(620)

	def WiFiSpeedRate(self):
		try:
			while True:
				Net_IN1 = psutil.net_io_counters().bytes_recv
				Net_OUT1 = psutil.net_io_counters().bytes_sent
				time.sleep(0.8)
				Net_IN2 = psutil.net_io_counters().bytes_recv
				Net_OUT2 = psutil.net_io_counters().bytes_sent
				NETIN = '{}GB'.format(round((Net_IN2 - Net_IN1) / 1073741824, 1))
				if NETIN[0:2] == '0.':
					NETIN = '{}MB'.format(round((Net_IN2 - Net_IN1) / 1048576, 1))
					if NETIN[0:2] == '0.':
						NETIN = '{}KB'.format(round((Net_IN2 - Net_IN1) / 1024, 1))
						if NETIN[0:2] == '0.':
							NETIN = '{}B'.format((Net_IN2 - Net_IN1))
				NETOUT = '{}GB'.format(round((Net_OUT2 - Net_OUT1) / 1073741824, 1))
				if NETOUT[0:2] == '0.':
					NETOUT = '{}MB'.format(round((Net_OUT2 - Net_OUT1) / 1048576, 1))
					if NETOUT[0:2] == '0.':
						NETOUT = '{}KB'.format(round((Net_OUT2 - Net_OUT1) / 1024, 1))
						if NETOUT[0:2] == '0.':
							NETOUT = '{}B'.format((Net_OUT2 - Net_OUT1))
				self.network.setText('↓{} /s ↑{} /s'.format(NETIN, NETOUT))
		except:
			pass

	def CPUMontor(self):
		try:
			while True:
				self.cpu.setText('{}%'.format(psutil.cpu_percent(interval=0.8)))
		except:
			pass

	def MemoryMonitor(self):
		try:
			while True:
				self.memoryUsedCapacityPercent.setText('{}%'.format(psutil.virtual_memory().percent))
				time.sleep(0.8)
		except:
			pass

	def FreeMemory(self):
		try:
			while True:
				MemoryFree = '{}GB'.format(round(psutil.virtual_memory().available / 1073741824, 1))
				if MemoryFree[0:2] == '0.':
					MemoryFree = '{}MB'.format(round(psutil.virtual_memory().available / 1048576, 1))
					if MemoryFree[0:2] == '0.':
						MemoryFree = '{}KB'.format(round(psutil.virtual_memory().available / 1024, 1))
						if MemoryFree[0:2] == '0.':
							MemoryFree = '{}B'.format(psutil.virtual_memory().available)
				self.memoryFree.setText('空き容量: {}GB 中 約{}'.format(round(psutil.virtual_memory().total / 1073741824, 1), MemoryFree))
				time.sleep(0.8)
		except:
			pass

	def UsedMemory(self):
		try:
			while True:
				useMemory = '{}GB'.format(round(psutil.virtual_memory().used / 1073741824, 1))
				if useMemory[0:2] == '0.':
					useMemory = '{}MB'.format(round(psutil.virtual_memory().used / 1048576, 1))
					if useMemory[0:2] == '0.':
						useMemory = '{}KB'.format(round(psutil.virtual_memory().used / 1024, 1))
						if useMemory[0:2] == '0.':
							useMemory = '{}B'.format(psutil.virtual_memory().used)
				self.memoryUsed.setText('使用容量: {}GB 中 約{}'.format(round(psutil.virtual_memory().total / 1073741824, 1), useMemory))
				time.sleep(0.8)
		except:
			pass

	def SwapMemoryUsedPercent(self):
		try:
			while True:
				self.virtualMemoryUsedCapacity.setText('{}%'.format(psutil.swap_memory().percent))
				time.sleep(0.8)
		except:
			pass

	def SwapUsed(self):
		try:
			while True:
				Swpused = '{}GB'.format(round(psutil.swap_memory().used / 1073741824, 1))
				if Swpused[0:2] == '0.':
					Swpused = '{}MB'.format(round(psutil.swap_memory().used / 1048576, 1))
					if Swpused[0:2] == '0.':
						Swpused = '{}KB'.format(round(psutil.swap_memory().used / 1024, 1))
						if Swpused[0:2] == '0.':
							Swpused = '{}B'.format(psutil.swap_memory().used)
				self.virtualMemoryUsed.setText('使用容量: {}GB 中 約{}'.format(round(psutil.swap_memory().total / 1073741824, 1), Swpused))
				time.sleep(0.8)
		except:
			pass

	def SwapFree(self):
		try:
			while True:
				SwpFree = '{}GB'.format(round(psutil.swap_memory().free / 1073741824, 1))
				if SwpFree[0:2] == '0.':
					SwpFree = '{}MB'.format(round(psutil.swap_memory().free / 1048576, 1))
					if SwpFree[0:2] == '0.':
						SwpFree = '{}KB'.format(round(psutil.swap_memory().free / 1024, 1))
						if SwpFree[0:2] == '0.':
							SwpFree = '{}B'.format(psutil.swap_memory().free)
				self.virtualMemoryFree.setText('空き容量: {}GB 中 約{}'.format(round(psutil.swap_memory().total / 1073741824, 1), SwpFree))
				time.sleep(0.8)
		except:
			pass

	def DiskUsedPercent(self):
		try:
			if not os.path.splitdrive(os.environ['windir'])[0] == '':
				mountPath = os.path.splitdrive(os.environ['windir'])[0] + '/'
			else:
				mountPath = '/'
		except KeyError:
			mountPath = '/'
		try:
			while True:
				self.diskUsedCapacity.setText('{}%'.format(psutil.disk_usage(mountPath).percent))
				time.sleep(0.8)
		except:
			pass

	def DiskUsed(self):
		try:
			if not os.path.splitdrive(os.environ['windir'])[0] == '':
				mountPath = os.path.splitdrive(os.environ['windir'])[0] + '/'
			else:
				mountPath = '/'
		except KeyError:
			mountPath = '/'
		try:
			TotalDisk = '{}TB'.format(round(psutil.disk_usage(mountPath).total / 1099511627776, 1))
			if TotalDisk[0:2] == '0.':
				TotalDisk = '{}GB'.format(round(psutil.disk_usage(mountPath).total / 1073741824, 1))
				if TotalDisk[0:2] == '0.':
					TotalDisk = '{}MB'.format(round(psutil.disk_usage(mountPath).total / 1048576, 1))
					if TotalDisk[0:2] == '0.':
						TotalDisk = '{}KB'.format(round(psutil.disk_usage(mountPath).total / 1024, 1))
						if TotalDisk[0:2] == '0.':
							TotalDisk = '{}B'.format(psutil.disk_usage(mountPath).total)
			while True:
				diskUseBytes = '{}TB'.format(round(psutil.disk_usage(mountPath).used / 1099511627776, 1))
				if diskUseBytes[0:2] == '0.':
					diskUseBytes = '{}GB'.format(round(psutil.disk_usage(mountPath).used / 1073741824, 1))
					if diskUseBytes[0:2] == '0.':
						diskUseBytes = '{}MB'.format(round(psutil.disk_usage(mountPath).used / 1048576, 1))
						if diskUseBytes[0:2] == '0.':
							diskUseBytes = '{}KB'.format(round(psutil.disk_usage(mountPath).used / 1024, 1))
							if diskUseBytes[0:2] == '0.':
								diskUseBytes = '{}B'.format(psutil.disk_usage(mountPath).used)
				self.diskUsed.setText('使用容量: 約{} 中 約{}'.format(TotalDisk, diskUseBytes))
				time.sleep(0.8)
		except:
			pass

	def DiskFree(self):
		try:
			if not os.path.splitdrive(os.environ['windir'])[0] == '':
				mountPath = os.path.splitdrive(os.environ['windir'])[0] + '/'
			else:
				mountPath = '/'
		except KeyError:
			mountPath = '/'
		try:
			TotalDisk = '{}TB'.format(round(psutil.disk_usage(mountPath).total / 1099511627776, 1))
			if TotalDisk[0:2] == '0.':
				TotalDisk = '{}GB'.format(round(psutil.disk_usage(mountPath).total / 1073741824, 1))
				if TotalDisk[0:2] == '0.':
					TotalDisk = '{}MB'.format(round(psutil.disk_usage(mountPath).total / 1048576, 1))
					if TotalDisk[0:2] == '0.':
						TotalDisk = '{}KB'.format(round(psutil.disk_usage(mountPath).total / 1024, 1))
						if TotalDisk[0:2] == '0.':
							TotalDisk = '{}B'.format(psutil.disk_usage(mountPath).total)
			while True:
				diskFreeBytes = '{}TB'.format(round(psutil.disk_usage(mountPath).free / 1099511627776, 1))
				if diskFreeBytes[0:2] == '0.':
					diskFreeBytes = '{}GB'.format(round(psutil.disk_usage(mountPath).free / 1073741824, 1))
					if diskFreeBytes[0:2] == '0.':
						diskFreeBytes = '{}MB'.format(round(psutil.disk_usage(mountPath).free / 1048576, 1))
						if diskFreeBytes[0:2] == '0.':
							diskFreeBytes = '{}KB'.format(round(psutil.disk_usage(mountPath).free / 1024, 1))
							if diskFreeBytes[0:2] == '0.':
								diskFreeBytes = '{}KB'.format(psutil.disk_usage(mountPath).free)
				self.diskFree.setText('空き容量: 約{} 中 約{}'.format(TotalDisk, diskFreeBytes))
				time.sleep(0.8)
		except:
			pass

class DiskPieWidget(QWidget):
	def __init__(self):
		super(DiskPieWidget, self).__init__()
		OutOfThread0.started.connect(self.updateSet)
		self.setStyleSheet('QWidget{background-color: #292828;color: #ededed;border: 0px #292828;}')
		self.setGraph()

	def updateSet(self):
		self.DataUpdate = QTimer()
		self.DataUpdate.timeout.connect(self.setGraph)
		self.DataUpdate.start(5000)

	def setGraph(self):
		DiskWidgets = []
		for idx, devices in enumerate(sorted(psutil.disk_partitions())):
			try:
				DevceName = devices.device
				MountPosition = devices.mountpoint
				devInfo = psutil.disk_usage(MountPosition)
				UsedRegion = round(devInfo.used / devInfo.total * 100)
				FreeRegion = round(devInfo.free / devInfo.total * 100)
				DeviceSerises = QPieSeries()
				DeviceSerises.clear()
				DeviceSerises.append('使用領域', UsedRegion)
				DeviceSerises.append('空き領域', FreeRegion)
				DeviceSerises.setHorizontalPosition(0.4999)
				DeviceSerises.setVerticalPosition(0.62)
				DeviceSerises.setPieSize(0.5)
				DeviceRegionLabelFont = QFont()
				DeviceRegionLabelFont.setPixelSize(8)
				DeviceSerises.slices()[0].setLabelFont(DeviceRegionLabelFont)
				DeviceSerises.slices()[0].setLabelBrush(QColor(237, 237, 237))
				DeviceSerises.slices()[0].setBrush(QColor(233, 88, 88))
				DeviceSerises.slices()[0].setLabel('使用領域 ({}%)'.format(round(100 * DeviceSerises.slices()[0].percentage())))
				DeviceSerises.slices()[0].setLabelPosition(QPieSlice.LabelInsideHorizontal)
				DeviceSerises.slices()[1].setLabelFont(DeviceRegionLabelFont)
				DeviceSerises.slices()[1].setLabelBrush(QColor(237, 237, 237))
				DeviceSerises.slices()[1].setBrush(QColor(39, 128, 219))
				DeviceSerises.slices()[1].setLabel('空き領域 ({}%)'.format(round(100 * DeviceSerises.slices()[1].percentage())))
				DeviceChart = QChart()
				DeviceChart.setBackgroundBrush(QColor(41, 40, 40))
				DeviceChart.addSeries(DeviceSerises)
				DeviceChart.setFont(DeviceRegionLabelFont)
				DeviceChart.legend().setVisible(True)
				DeviceChart.legend().setAlignment(Qt.AlignBottom)
				DeviceChart.legend().setLabelBrush(QColor(237, 237, 237))
				DeviceChart.setMaximumSize(300, 100)
				DeviceChart.setContentsMargins(-200, -58, -215, -38)
				DeviceChartView = QChartView(DeviceChart)
				DeviceChartView.setObjectName('DiskChart_{}'.format(idx))
				DeviceChartView.setStyleSheet('QChartView#DiskChart_%s{background-color: #292828;}' % str(idx))
				DeviceChartView.setFont(DeviceRegionLabelFont)
				DeviceChartView.setMaximumWidth(600)
				DeviceChartView.setMaximumHeight(500)
				DeviceChartView.setContentsMargins(0, 0, 20, 0)
				DeviceChartView.setAlignment(Qt.AlignCenter)
				DeviceChart.setBackgroundRoundness(0)
				DiskWidgets.append([DeviceChartView, DevceName])
			except:
				pass
		self.DiskWdget = QGridLayout()
		self.colmunsCount = [_c for _c in range(len(DiskWidgets))]
		self.delmiterColmun = []
		DmiterCount0 = []
		DmiterCount1 = []
		for ix in range(0, len(self.colmunsCount), 2):
			try:
				self.delmiterColmun.append(self.colmunsCount[ix:ix + 2])
			except:
				continue
		for d0 in self.delmiterColmun:
			try:
				DmiterCount0.append(d0[1])
			except:
				continue
		for d1 in self.delmiterColmun:
			try:
				DmiterCount1.append(d1[0])
			except:
				continue
		row = 0
		col = 0
		for idx, DeviceWidget in enumerate(DiskWidgets):
			if idx in DmiterCount1:
				row = 0
				col = idx + 1
			elif idx in DmiterCount0:
				row = 1
				col = idx
			self.DiskWdget.addWidget(DeviceWidget[0], row, col, Qt.AlignLeft)
			self.DiskWdget.setContentsMargins(0, 0, 10, 0)
			self.DiskLabelList = QListView()
			self.DiskLabelList.setStyleSheet('QListView{background-color: #292828;color: #ededed;border: 0px #292828;}')
			self.DiskLabel0 = QLabel()
			self.DiskLabel0.setPixmap(QFileIconProvider().icon(QFileIconProvider.Drive).pixmap(QSize(32, 32)))
			self.DiskLabel0.setStyleSheet('QLabel{background-color: #292828;color: #ededed;}')
			self.DiskLabel0.setAlignment(Qt.AlignLeft)
			self.DiskLabel1Font = QFont()
			self.DiskLabel1Font.setPixelSize(25)
			self.DiskLabel1 = QLabel()
			self.DiskLabel1.setAlignment(Qt.AlignLeft)
			self.DiskLabel1.setText(DeviceWidget[1])
			self.DiskLabel1.setStyleSheet('QLabel{background-color: #292828;color: #ededed;}')
			self.DiskLabel1.setFont(self.DiskLabel1Font)
			self.DiskSpaceFont = QFont()
			self.DiskSpaceFont.setPixelSize(1)
			self.DiskSpace = QLabel()
			self.DiskSpace.setAlignment(Qt.AlignLeft)
			self.DiskSpace.setText(' ')
			self.DiskSpace.setStyleSheet('QLabel{background-color: #292828;color: #ededed;}')
			self.DiskSpace.setFont(self.DiskLabel1Font)
			self.DiskLabelSubWidget = QGridLayout()
			self.DiskLabelSubWidget.addWidget(self.DiskLabel1, 0, 3, Qt.AlignLeft)
			self.DiskLabelSubWidget.addWidget(self.DiskLabel0, 0, 1, Qt.AlignLeft)
			self.DiskLabelSubWidget.addWidget(self.DiskSpace, 0, 2, Qt.AlignLeft)
			self.DiskLabelList.setIconSize(QSize(25, 25))
			self.DiskLabelList.setLayout(self.DiskLabelSubWidget)
			self.DiskLabelList.setMaximumWidth(247)
			self.DiskLabelList.setMinimumHeight(10)
			self.DiskWdget.addWidget(self.DiskLabelList, row + 1, col, Qt.AlignLeft)
			col = col + idx
		self.setLayout(self.DiskWdget)

class EditMusicTagDailog(QDialog):
	def __init__(self, SelectedFilePath):
		super(EditMusicTagDailog, self).__init__()
		self.FilePathList = SelectedFilePath
		self.setWindowTitle('ファイルの詳細')
		self.setFixedSize(530, 680)
		DropedCheck[0] = '0'
		self.FilesCount = 0
		self.FoldersCount = 0
		self.Files = []
		self.OtherFiles = []
		self.Folders = []
		EditMediaPath_FLAC[0:] = []
		EditMediaPath_M4A[0:] = []
		EditMediaPath_MP3[0:] = []
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.FilePropertyTab = QTabWidget(self)
		self.FilePropertyTab.setFixedSize(490, 615)
		self.FilePropertyTab.setStyleSheet('QWidget{background-color: #2d2d2d;color: #ededed;} QTabBar::tab{background-color: #2d2d2d;color: White;border: 1px solid #1a1a1a;border-color: #1a1a1a;} QTabWidget::pane{background-color: #2d2d2d;color: #ededed;} QTabWidget::tab{border: 0px solid #1a1a1a;border-color: #1a1a1a;background-color: #2d2d2d;#ededed;}')
		if len(self.FilePathList) == 1:
			self.OhterMultipleFileCheck = False
			self.MultipleFileCheck = True
			self.GeneralTab = QWidget()
			self.PreviewIcon = QLabel(self.GeneralTab)
			self.PreviewIcon.setGeometry(QRect(35, 0, 70, 70))
			self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileName = QLineEdit(self.GeneralTab)
			self.FileName.setGeometry(QRect(160, 20, 310, 30))
			self.FileName.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
			self.BorderFrame1 = QLabel(self.GeneralTab)
			self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
			self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
			self.FileTypeLabel = QLabel('ファイルの種類:', self.GeneralTab)
			self.FileTypeLabel.setGeometry(QRect(20, 115, 110, 30))
			self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileType = QLabel(self.GeneralTab)
			self.FileType.setGeometry(QRect(160, 115, 310, 30))
			self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.BorderFrame2 = QLabel(self.GeneralTab)
			self.BorderFrame2.setGeometry(QRect(20, 175, 450, 1))
			self.BorderFrame2.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
			self.FilePathLabel = QLabel('場所:', self.GeneralTab)
			self.FilePathLabel.setGeometry(QRect(20, 205, 50, 30)) # label only x 30, y50ずつ
			self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FilePath = QLabel(self.GeneralTab)
			self.FilePath.setGeometry(QRect(160, 205, 350, 30))
			self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
			self.FileSizeLabel.setGeometry(QRect(20, 260, 60, 30))
			self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileSize = QLabel(self.GeneralTab)
			self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileSize.setGeometry(QRect(160, 260, 350, 30))
			self.BorderFrame3 = QLabel(self.GeneralTab)
			self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
			self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
			self.FileCreateDaylabel = QLabel('作成日時:', self.GeneralTab)
			self.FileCreateDaylabel.setGeometry(QRect(20, 360, 70, 30))
			self.FileCreateDaylabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileCreateDay = QLabel(self.GeneralTab)
			self.FileCreateDay.setGeometry(QRect(160, 360, 350, 30))
			self.FileCreateDay.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileModifiedLabel = QLabel('更新日時:', self.GeneralTab)
			self.FileModifiedLabel.setGeometry(QRect(20, 425, 70, 30))
			self.FileModifiedLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.FileModifiedTime = QLabel(self.GeneralTab)
			self.FileModifiedTime.setGeometry(QRect(160, 425, 350, 30))
			self.FileModifiedTime.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.LastAccessLabel = QLabel('アクセス日時:', self.GeneralTab)
			self.LastAccessLabel.setGeometry(QRect(20, 490, 100, 30))
			self.LastAccessLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.LastAccessTime = QLabel(self.GeneralTab)
			self.LastAccessTime.setGeometry(QRect(160, 490, 350, 30))
			self.LastAccessTime.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
			self.BorderFrame4 = QLabel(self.GeneralTab)
			self.BorderFrame4.setGeometry(QRect(20, 560, 450, 1))
			self.BorderFrame4.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
			self.FilePropertyTab.addTab(self.GeneralTab, '')
			if self.FilePathList[0].lower().endswith(('.flac', '.m4a', '.mp3')):
				self.OhterMultipleFileCheck = False
				self.MultipleFileCheck = True
				self.DetailInfoTab = QWidget()
				self.TrackNameLabel = QLabel('タイトル', self.DetailInfoTab)
				self.TrackNameLabel.setGeometry(QRect(20, 10, 80, 30))
				self.TrackNameLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackName = QLineEdit(self.DetailInfoTab)
				self.TrackName.setGeometry(QRect(190, 10, 280, 30))
				self.TrackName.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtistLabel = QLabel('アーティスト', self.DetailInfoTab)
				self.TrackArtistLabel.setGeometry(QRect(20, 65, 110, 30))
				self.TrackArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArtist = QLineEdit(self.DetailInfoTab)
				self.TrackArtist.setGeometry(QRect(190, 65, 280, 30))
				self.TrackArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbumArtistLabel = QLabel('アルバムアーティスト', self.DetailInfoTab)
				self.TrackAlbumArtistLabel.setGeometry(QRect(20, 125, 150, 30))
				self.TrackAlbumArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumArtist = QLineEdit(self.DetailInfoTab)
				self.TrackAlbumArtist.setGeometry(QRect(190, 125, 280, 30))
				self.TrackAlbumArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbumLabel = QLabel('アルバム名', self.DetailInfoTab)
				self.TrackAlbumLabel.setGeometry(QRect(20, 185, 150, 30))
				self.TrackAlbumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbum = QLineEdit(self.DetailInfoTab)
				self.TrackAlbum.setGeometry(QRect(190, 185, 280, 30))
				self.TrackAlbum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackGenreLabel = QLabel('ジャンル', self.DetailInfoTab)
				self.TrackGenreLabel.setGeometry(QRect(20, 245, 150, 30))
				self.TrackGenreLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackGenre = QLineEdit(self.DetailInfoTab)
				self.TrackGenre.setGeometry(QRect(190, 245, 280, 30))
				self.TrackGenre.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackYearLabel = QLabel('リリース日時', self.DetailInfoTab)
				self.TrackYearLabel.setGeometry(QRect(20, 305, 150, 30))
				self.TrackYearLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackYear = QLineEdit(self.DetailInfoTab)
				self.TrackYear.setGeometry(QRect(190, 305, 280, 30))
				self.TrackYear.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;}')
				self.TrackNumlabel = QLabel('トラック番号', self.DetailInfoTab)
				self.TrackNumlabel.setGeometry(QRect(20, 365, 150, 30))
				self.TrackNumlabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackNum = QLineEdit(self.DetailInfoTab)
				self.TrackNum.setGeometry(QRect(190, 365, 280, 30))
				self.TrackNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackDiscNumLabel = QLabel('ディスク番号', self.DetailInfoTab)
				self.TrackDiscNumLabel.setGeometry(QRect(20, 425, 150, 30))
				self.TrackDiscNumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackDiscNum = QLineEdit(self.DetailInfoTab)
				self.TrackDiscNum.setGeometry(QRect(190, 425, 280, 30))
				self.TrackDiscNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtLabel = QLabel('アルバムカバー', self.DetailInfoTab)
				self.TrackArtLabel.setGeometry(QRect(70, 515, 110, 30))
				self.TrackArtLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArt = EditCoverArtLabel(self.DetailInfoTab)
				self.TrackArt.setGeometry(QRect(280, 480, 100, 100))
				self.TrackArt.setAcceptDrops(True)
				self.FilePropertyTab.addTab(self.DetailInfoTab, '')
				self.FilePropertyTab.setTabText(self.FilePropertyTab.indexOf(self.DetailInfoTab), '詳細')
		elif 2 <= len(self.FilePathList):
			for MediaOnly in self.FilePathList:
				if MediaOnly.lower().endswith('.flac'):
					EditMediaPath_FLAC.append(MediaOnly)
				if MediaOnly.lower().endswith('.m4a'):
					EditMediaPath_M4A.append(MediaOnly)
				if MediaOnly.lower().endswith('.mp3'):
					EditMediaPath_MP3.append(MediaOnly)
				if QFileInfo(MediaOnly).isFile():
					self.Files.append(MediaOnly)
				if QFileInfo(MediaOnly).isDir():
					self.Folders.append(MediaOnly)
				if not MediaOnly.lower().endswith(('.flac', '.m4a', '.mp3')):
					self.OtherFiles.append(MediaOnly)
			self.FilesCount = len(self.Files)
			self.FoldersCount = len(self.Folders)
			if not len(EditMediaPath_FLAC) == 0 and not len(EditMediaPath_M4A) == 0 and not len(EditMediaPath_MP3) == 0 and not len(self.OtherFiles) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_FLAC) == 0 and not len(EditMediaPath_M4A) == 0 and not len(EditMediaPath_MP3) == 0 and not self.FoldersCount == 0 and not len(self.OtherFiles) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_FLAC) == 0 and not len(self.OtherFiles) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_M4A) == 0 and not len(self.OtherFiles) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_MP3) == 0 and not len(self.OtherFiles) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_FLAC) == 0 and not self.FoldersCount == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_M4A) == 0 and not self.FoldersCount == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_MP3) == 0 and not self.FoldersCount == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(self.OtherFiles) == 0 and not self.FoldersCount == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_FLAC) == 0 and not len(EditMediaPath_M4A) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_FLAC) == 0 and not len(EditMediaPath_MP3) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif not len(EditMediaPath_M4A) == 0 and not len(EditMediaPath_MP3) == 0: # 複数の種類
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			elif 2 <= len(self.OtherFiles):
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数の種類')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
			if not len(EditMediaPath_FLAC) == 0 and len(EditMediaPath_M4A) == 0 and len(EditMediaPath_MP3) == 0 and self.FoldersCount == 0 and len(self.OtherFiles) == 0: # 複数のFLACファイル
				self.OhterMultipleFileCheck = False
				self.MultipleFileCheck = True
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数のFLACファイルのすべて')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
				self.DetailInfoTab = QWidget()
				self.TrackNameLabel = QLabel('タイトル', self.DetailInfoTab)
				self.TrackNameLabel.setGeometry(QRect(20, 10, 80, 30))
				self.TrackNameLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackName = QLineEdit(self.DetailInfoTab)
				self.TrackName.setText('(複数の値)')
				self.TrackName.setGeometry(QRect(190, 10, 280, 30))
				self.TrackName.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtistLabel = QLabel('アーティスト', self.DetailInfoTab)
				self.TrackArtistLabel.setGeometry(QRect(20, 65, 110, 30))
				self.TrackArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArtist = QLineEdit(self.DetailInfoTab)
				self.TrackArtist.setText('(複数の値)')
				self.TrackArtist.setGeometry(QRect(190, 65, 280, 30))
				self.TrackArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumArtistLabel = QLabel('アルバムアーティスト', self.DetailInfoTab)
				self.TrackAlbumArtistLabel.setGeometry(QRect(20, 125, 150, 30))
				self.TrackAlbumArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbumArtist = QLineEdit(self.DetailInfoTab)
				self.TrackAlbumArtist.setText('(複数の値)')
				self.TrackAlbumArtist.setGeometry(QRect(190, 125, 280, 30))
				self.TrackAlbumArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumLabel = QLabel('アルバム名', self.DetailInfoTab)
				self.TrackAlbumLabel.setGeometry(QRect(20, 185, 150, 30))
				self.TrackAlbumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbum = QLineEdit(self.DetailInfoTab)
				self.TrackAlbum.setText('(複数の値)')
				self.TrackAlbum.setGeometry(QRect(190, 185, 280, 30))
				self.TrackAlbum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackGenreLabel = QLabel('ジャンル', self.DetailInfoTab)
				self.TrackGenreLabel.setGeometry(QRect(20, 245, 150, 30))
				self.TrackGenreLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackGenre = QLineEdit(self.DetailInfoTab)
				self.TrackGenre.setText('(複数の値)')
				self.TrackGenre.setGeometry(QRect(190, 245, 280, 30))
				self.TrackGenre.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackYearLabel = QLabel('リリース日時', self.DetailInfoTab)
				self.TrackYearLabel.setGeometry(QRect(20, 305, 150, 30))
				self.TrackYearLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackYear = QLineEdit(self.DetailInfoTab)
				self.TrackYear.setText('(複数の値)')
				self.TrackYear.setGeometry(QRect(190, 305, 280, 30))
				self.TrackYear.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;}')
				self.TrackNumlabel = QLabel('トラック番号', self.DetailInfoTab)
				self.TrackNumlabel.setGeometry(QRect(20, 365, 150, 30))
				self.TrackNumlabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackNum = QLineEdit(self.DetailInfoTab)
				self.TrackNum.setText('(複数の値)')
				self.TrackNum.setGeometry(QRect(190, 365, 280, 30))
				self.TrackNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackDiscNumLabel = QLabel('ディスク番号', self.DetailInfoTab)
				self.TrackDiscNumLabel.setGeometry(QRect(20, 425, 150, 30))
				self.TrackDiscNumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackDiscNum = QLineEdit(self.DetailInfoTab)
				self.TrackDiscNum.setText('(複数の値)')
				self.TrackDiscNum.setGeometry(QRect(190, 425, 280, 30))
				self.TrackDiscNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtLabel = QLabel('アルバムカバー', self.DetailInfoTab)
				self.TrackArtLabel.setGeometry(QRect(70, 515, 110, 30))
				self.TrackArtLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArt = EditCoverArtLabel(self.DetailInfoTab)
				self.TrackArt.setGeometry(QRect(280, 480, 100, 100))
				self.TrackArt.setAcceptDrops(True)
				self.FilePropertyTab.addTab(self.DetailInfoTab, '')
				self.FilePropertyTab.setTabText(self.FilePropertyTab.indexOf(self.DetailInfoTab), '詳細')
			elif len(EditMediaPath_FLAC) == 0 and not len(EditMediaPath_M4A) == 0 and len(EditMediaPath_MP3) == 0 and self.FoldersCount == 0 and len(self.OtherFiles) == 0: # 複数のM4Aファイル
				self.OhterMultipleFileCheck = False
				self.MultipleFileCheck = True
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数のM4Aファイルのすべて')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
				self.DetailInfoTab = QWidget()
				self.TrackNameLabel = QLabel('タイトル', self.DetailInfoTab)
				self.TrackNameLabel.setGeometry(QRect(20, 10, 80, 30))
				self.TrackNameLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackName = QLineEdit(self.DetailInfoTab)
				self.TrackName.setText('(複数の値)')
				self.TrackName.setGeometry(QRect(190, 10, 280, 30))
				self.TrackName.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtistLabel = QLabel('アーティスト', self.DetailInfoTab)
				self.TrackArtistLabel.setGeometry(QRect(20, 65, 110, 30))
				self.TrackArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArtist = QLineEdit(self.DetailInfoTab)
				self.TrackArtist.setText('(複数の値)')
				self.TrackArtist.setGeometry(QRect(190, 65, 280, 30))
				self.TrackArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumArtistLabel = QLabel('アルバムアーティスト', self.DetailInfoTab)
				self.TrackAlbumArtistLabel.setGeometry(QRect(20, 125, 150, 30))
				self.TrackAlbumArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbumArtist = QLineEdit(self.DetailInfoTab)
				self.TrackAlbumArtist.setText('(複数の値)')
				self.TrackAlbumArtist.setGeometry(QRect(190, 125, 280, 30))
				self.TrackAlbumArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumLabel = QLabel('アルバム名', self.DetailInfoTab)
				self.TrackAlbumLabel.setGeometry(QRect(20, 185, 150, 30))
				self.TrackAlbumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbum = QLineEdit(self.DetailInfoTab)
				self.TrackAlbum.setText('(複数の値)')
				self.TrackAlbum.setGeometry(QRect(190, 185, 280, 30))
				self.TrackAlbum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;}')
				self.TrackGenreLabel = QLabel('ジャンル', self.DetailInfoTab)
				self.TrackGenreLabel.setGeometry(QRect(20, 245, 150, 30))
				self.TrackGenreLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackGenre = QLineEdit(self.DetailInfoTab)
				self.TrackGenre.setText('(複数の値)')
				self.TrackGenre.setGeometry(QRect(190, 245, 280, 30))
				self.TrackGenre.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackYearLabel = QLabel('リリース日時', self.DetailInfoTab)
				self.TrackYearLabel.setGeometry(QRect(20, 305, 150, 30))
				self.TrackYearLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackYear = QLineEdit(self.DetailInfoTab)
				self.TrackYear.setText('(複数の値)')
				self.TrackYear.setGeometry(QRect(190, 305, 280, 30))
				self.TrackYear.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackNumlabel = QLabel('トラック番号', self.DetailInfoTab)
				self.TrackNumlabel.setGeometry(QRect(20, 365, 150, 30))
				self.TrackNumlabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackNum = QLineEdit(self.DetailInfoTab)
				self.TrackNum.setText('(複数の値)')
				self.TrackNum.setGeometry(QRect(190, 365, 280, 30))
				self.TrackNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackDiscNumLabel = QLabel('ディスク番号', self.DetailInfoTab)
				self.TrackDiscNumLabel.setGeometry(QRect(20, 425, 150, 30))
				self.TrackDiscNumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackDiscNum = QLineEdit(self.DetailInfoTab)
				self.TrackDiscNum.setText('(複数の値)')
				self.TrackDiscNum.setGeometry(QRect(190, 425, 280, 30))
				self.TrackDiscNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtLabel = QLabel('アルバムカバー', self.DetailInfoTab)
				self.TrackArtLabel.setGeometry(QRect(70, 515, 110, 30))
				self.TrackArtLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArt = EditCoverArtLabel(self.DetailInfoTab)
				self.TrackArt.setGeometry(QRect(280, 480, 100, 100))
				self.TrackArt.setAcceptDrops(True)
				self.FilePropertyTab.addTab(self.DetailInfoTab, '')
				self.FilePropertyTab.setTabText(self.FilePropertyTab.indexOf(self.DetailInfoTab), '詳細')
			elif len(EditMediaPath_FLAC) == 0 and len(EditMediaPath_M4A) == 0 and not len(EditMediaPath_MP3) == 0 and self.FoldersCount == 0 and len(self.OtherFiles) == 0: # 複数のMP3ファイル
				self.OhterMultipleFileCheck = False
				self.MultipleFileCheck = True
				self.OhterMultipleFileCheck = True
				self.MultipleFileCheck = False
				self.GeneralTab = QWidget()
				self.PreviewIcon = QLabel(self.GeneralTab)
				self.PreviewIcon.setGeometry(QRect(35, 0, 57, 57))
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(57, 57)))
				self.PreviewIcon.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.PreviewIcon2 = QLabel(self.GeneralTab)
				self.PreviewIcon2.setGeometry(QRect(28, 7, 55, 55))
				self.PreviewIcon2.setPixmap(QFileIconProvider().icon(QFileIconProvider.File).pixmap(QSize(55, 55)))
				self.PreviewIcon2.setStyleSheet('QLabel{background-color: rba(45, 45, 45, 45);color: #ededed;}')
				self.FileName = QLabel(self.GeneralTab)
				self.FileName.setGeometry(QRect(160, 20, 310, 30))
				self.FileName.setText('ファイル数: {}、フォルダー数: {}'.format(self.FilesCount, self.FoldersCount))
				self.FileName.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.BorderFrame1 = QLabel(self.GeneralTab)
				self.BorderFrame1.setGeometry(QRect(20, 85, 450, 1))
				self.BorderFrame1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FileTypeLabel = QLabel('種類:', self.GeneralTab)
				self.FileTypeLabel.setGeometry(QRect(20, 115, 80, 30))
				self.FileTypeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileType = QLabel(self.GeneralTab)
				self.FileType.setText('複数のMP3ファイルのすべて')
				self.FileType.setGeometry(QRect(160, 115, 310, 30))
				self.FileType.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePathLabel = QLabel('場所:', self.GeneralTab)
				self.FilePathLabel.setGeometry(QRect(20, 175, 50, 30))  # label only x 30, y50ずつ
				self.FilePathLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FilePath = QLabel(self.GeneralTab)
				self.FilePath.setGeometry(QRect(160, 175, 350, 30))
				self.FilePath.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSizeLabel = QLabel('サイズ:', self.GeneralTab)
				self.FileSizeLabel.setGeometry(QRect(20, 245, 60, 30))
				self.FileSizeLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize = QLabel(self.GeneralTab)
				self.FileSize.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.FileSize.setGeometry(QRect(160, 245, 350, 30))
				self.BorderFrame3 = QLabel(self.GeneralTab)
				self.BorderFrame3.setGeometry(QRect(20, 325, 450, 1))
				self.BorderFrame3.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
				self.FilePropertyTab.addTab(self.GeneralTab, '')
				self.DetailInfoTab = QWidget()
				self.TrackNameLabel = QLabel('タイトル', self.DetailInfoTab)
				self.TrackNameLabel.setGeometry(QRect(20, 10, 80, 30))
				self.TrackNameLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackName = QLineEdit(self.DetailInfoTab)
				self.TrackName.setText('(複数の値)')
				self.TrackName.setGeometry(QRect(190, 10, 280, 30))
				self.TrackName.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtistLabel = QLabel('アーティスト', self.DetailInfoTab)
				self.TrackArtistLabel.setGeometry(QRect(20, 65, 110, 30))
				self.TrackArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArtist = QLineEdit(self.DetailInfoTab)
				self.TrackArtist.setText('(複数の値)')
				self.TrackArtist.setGeometry(QRect(190, 65, 280, 30))
				self.TrackArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumArtistLabel = QLabel('アルバムアーティスト', self.DetailInfoTab)
				self.TrackAlbumArtistLabel.setGeometry(QRect(20, 125, 150, 30))
				self.TrackAlbumArtistLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbumArtist = QLineEdit(self.DetailInfoTab)
				self.TrackAlbumArtist.setText('(複数の値)')
				self.TrackAlbumArtist.setGeometry(QRect(190, 125, 280, 30))
				self.TrackAlbumArtist.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackAlbumLabel = QLabel('アルバム名', self.DetailInfoTab)
				self.TrackAlbumLabel.setGeometry(QRect(20, 185, 150, 30))
				self.TrackAlbumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackAlbum = QLineEdit(self.DetailInfoTab)
				self.TrackAlbum.setText('(複数の値)')
				self.TrackAlbum.setGeometry(QRect(190, 185, 280, 30))
				self.TrackAlbum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackGenreLabel = QLabel('ジャンル', self.DetailInfoTab)
				self.TrackGenreLabel.setGeometry(QRect(20, 245, 150, 30))
				self.TrackGenreLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackGenre = QLineEdit(self.DetailInfoTab)
				self.TrackGenre.setText('(複数の値)')
				self.TrackGenre.setGeometry(QRect(190, 245, 280, 30))
				self.TrackGenre.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackYearLabel = QLabel('リリース日時', self.DetailInfoTab)
				self.TrackYearLabel.setGeometry(QRect(20, 305, 150, 30))
				self.TrackYearLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackYear = QLineEdit(self.DetailInfoTab)
				self.TrackYear.setText('(複数の値)')
				self.TrackYear.setGeometry(QRect(190, 305, 280, 30))
				self.TrackYear.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackNumlabel = QLabel('トラック番号', self.DetailInfoTab)
				self.TrackNumlabel.setGeometry(QRect(20, 365, 150, 30))
				self.TrackNumlabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackNum = QLineEdit(self.DetailInfoTab)
				self.TrackNum.setText('(複数の値)')
				self.TrackNum.setGeometry(QRect(190, 365, 280, 30))
				self.TrackNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackDiscNumLabel = QLabel('ディスク番号', self.DetailInfoTab)
				self.TrackDiscNumLabel.setGeometry(QRect(20, 425, 150, 30))
				self.TrackDiscNumLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackDiscNum = QLineEdit(self.DetailInfoTab)
				self.TrackDiscNum.setText('(複数の値)')
				self.TrackDiscNum.setGeometry(QRect(190, 425, 280, 30))
				self.TrackDiscNum.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
				self.TrackArtLabel = QLabel('アルバムカバー', self.DetailInfoTab)
				self.TrackArtLabel.setGeometry(QRect(70, 515, 110, 30))
				self.TrackArtLabel.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
				self.TrackArt = EditCoverArtLabel(self.DetailInfoTab)
				self.TrackArt.setGeometry(QRect(280, 480, 100, 100))
				self.TrackArt.setAcceptDrops(True)
				self.FilePropertyTab.addTab(self.DetailInfoTab, '')
				self.FilePropertyTab.setTabText(self.FilePropertyTab.indexOf(self.DetailInfoTab), '詳細')
		self.FilePropertyTab.setTabText(self.FilePropertyTab.indexOf(self.GeneralTab), '全般')
		self.CheckOkButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.CheckOkButton.rejected.connect(self.reject)
		self.CheckOkButton.accepted.connect(self.accept)
		self.CheckOkButton.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.FilePropertyTab.setCurrentIndex(0)
		self.PropertyLayouts = QGridLayout()
		self.PropertyLayouts.addWidget(self.FilePropertyTab)
		self.PropertyLayouts.addWidget(self.CheckOkButton)
		self.setLayout(self.PropertyLayouts)
		self.LoadMetadata()

	def LoadMetadata(self):
		if len(self.FilePathList) == 1:
			self.setWindowTitle('{}のプロパティ'.format(self.FilePathList[0].split('/')[-1]))
			FolderFilePath = QFileInfo(self.FilePathList[0])
			self.setWindowIcon(QFileIconProvider().icon(FolderFilePath).pixmap(QSize(16, 16)))
			if platform.system() == 'Windows':
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(FolderFilePath).pixmap(QSize(64, 64)).scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation))
			else:
				self.PreviewIcon.setPixmap(QFileIconProvider().icon(FolderFilePath).pixmap(QSize(57, 57)))
			self.FileName.setText(FolderFilePath.fileName())
			if FolderFilePath.isFile():
				self.FileType.setText('{}ファイル (.{})'.format(FolderFilePath.suffix().upper(), FolderFilePath.suffix().lower()))
				if self.FileType.text() == 'ファイル (.)':
					self.FileType.setText('ファイル')
			else:
				self.FileType.setText('ファイルフォルダ')
			self.FilePath.setText(FolderFilePath.path())
			FileFolderSize = '{}GB'.format(str(round(FolderFilePath.size() / 1073741824, 2)))
			if FileFolderSize[0:2] == '0.':
				FileFolderSize = '{}MB'.format(str(round(FolderFilePath.size() / 1048576, 2)))
				if FileFolderSize[0:2] == '0.':
					FileFolderSize = '{}KB'.format(str(round(FolderFilePath.size() / 1024, 2)))
					if FileFolderSize[0:2] == '0.':
						FileFolderSize = '{}B'.format(str(round(FolderFilePath.size(), 2)))
						if FileFolderSize[0:2] == '0.':
							FileFolderSize = '不明なサイズ'
			self.FileSize.setText(FileFolderSize)
			try:
				if platform.system() == 'Windows':
					if not datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_ctime).strftime('%Y年%m月%d日 %I:%M:%S') == '':
						self.FileCreateDay.setText(datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_ctime).strftime('%Y年%m月%d日 %I:%M:%S'))
					else:
						self.FileCreateDay.setText('不明')
				else:
					if not datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_birthtime).strftime('%Y年%m月%d日 %I:%M:%S') == '':
						self.FileCreateDay.setText(datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_birthtime).strftime('%Y年%m月%d日 %I:%M:%S'))
					else:
						self.FileCreateDay.setText('不明')
			except:
				pass
			try:
				if not datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_mtime).strftime('%Y年%m月%d日 %I:%M:%S') == '':
					self.FileModifiedTime.setText(datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_mtime).strftime('%Y年%m月%d日 %I:%M:%S'))
				else:
					self.FileModifiedTime.setText('不明')
			except:
				pass
			try:
				if not datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_atime).strftime('%Y年%m月%d日 %I:%M:%S') == '':
					self.LastAccessTime.setText(datetime.datetime.fromtimestamp(os.stat(self.FilePathList[0]).st_atime).strftime('%Y年%m月%d日 %I:%M:%S'))
				else:
					self.LastAccessTime.setText('不明')
			except:
				pass
			if self.FilePathList[0].lower().endswith('.flac'):
				try:
					self.TrackName.setText(mutagen.flac.FLAC(self.FilePathList[0])['title'][0])
				except:
					pass
				try:
					self.TrackArtist.setText(mutagen.flac.FLAC(self.FilePathList[0])['artist'][0])
				except:
					pass
				try:
					self.TrackAlbumArtist.setText(mutagen.flac.FLAC(self.FilePathList[0])['albumartist'][0])
				except:
					pass
				try:
					self.TrackAlbum.setText(mutagen.flac.FLAC(self.FilePathList[0])['album'][0])
				except:
					pass
				try:
					self.TrackGenre.setText(mutagen.flac.FLAC(self.FilePathList[0])['genre'][0])
				except:
					pass
				try:
					self.TrackYear.setText(mutagen.flac.FLAC(self.FilePathList[0])['date'][0])
				except:
					pass
				try:
					self.TrackNum.setText(mutagen.flac.FLAC(self.FilePathList[0])['tracknumber'][0])
				except:
					pass
				try:
					self.TrackDiscNum.setText('{} / {}'.format(mutagen.flac.FLAC(self.FilePathList[0])['discnumber'][0], mutagen.flac.FLAC(self.FilePathList[0])['disctotal'][0]))
				except:
					pass
				try:
					self.TrackArt.setPixmap(QPixmap().fromImage(QImage.fromData(mutagen.flac.FLAC(self.FilePathList[0]).pictures[0].data)).scaled(100, 100, Qt.KeepAspectRatio))
				except:
					pass
			if self.FilePathList[0].lower().endswith('.m4a'):
				try:
					self.TrackName.setText(mutagen.mp4.MP4(self.FilePathList[0])['\xa9nam'][0])
				except:
					pass
				try:
					self.TrackArtist.setText(mutagen.mp4.MP4(self.FilePathList[0])['\xa9ART'][0])
				except:
					pass
				try:
					self.TrackAlbumArtist.setText(mutagen.mp4.MP4(self.FilePathList[0])['aART'][0])
				except:
					pass
				try:
					self.TrackAlbum.setText(mutagen.mp4.MP4(self.FilePathList[0])['\xa9alb'][0])
				except:
					pass
				try:
					self.TrackGenre.setText(mutagen.mp4.MP4(self.FilePathList[0])['\xa9gen'][0])
				except:
					pass
				try:
					self.TrackYear.setText(mutagen.mp4.MP4(self.FilePathList[0])['\xa9day'][0])
				except:
					pass
				try:
					TrackNum, TotalTrackNum = mutagen.mp4.MP4(self.FilePathList[0])['trkn'][0]
					self.TrackNum.setText('{} / {}'.format(str(TrackNum), str(TotalTrackNum)))
				except:
					pass
				try:
					DiscNum, TotalDisc = mutagen.mp4.MP4(self.FilePathList[0])['disk'][0]
					self.TrackDiscNum.setText('{} / {}'.format(DiscNum, TotalDisc))
				except:
					pass
				try:
					self.TrackArt.setPixmap(QPixmap().fromImage(QImage.fromData(mutagen.mp4.MP4(self.FilePathList[0])['covr'][0])).scaled(100, 100, Qt.KeepAspectRatio))
				except:
					pass
			if self.FilePathList[0].lower().endswith('.mp3'):
				try:
					self.TrackName.setText(EasyID3(self.FilePathList[0])['title'][0])
				except:
					pass
				try:
					self.TrackArtist.setText(EasyID3(self.FilePathList[0])['artist'][0])
				except:
					pass
				try:
					self.TrackAlbumArtist.setText(EasyID3(self.FilePathList[0])['albumartist'][0])
				except:
					pass
				try:
					self.TrackAlbum.setText(EasyID3(self.FilePathList[0])['album'][0])
				except:
					pass
				try:
					self.TrackGenre.setText(EasyID3(self.FilePathList[0])['genre'][0])
				except:
					pass
				try:
					self.TrackYear.setText(EasyID3(self.FilePathList[0])['date'][0])
				except:
					pass
				try:
					TrackNum, TotalTrackNum = EasyID3(self.FilePathList[0])['tracknumber'][0]
					self.TrackNum.setText('{} / {}'.format(str(TrackNum), str(TotalTrackNum)))
				except:
					pass
				try:
					DiscNum, TotalDisc = EasyID3(self.FilePathList[0])['discnumber'][0]
					self.TrackDiscNum.setText('{} / {}'.format(DiscNum, TotalDisc))
				except:
					pass
				try:
					self.TrackArt.setPixmap(QPixmap().fromImage(QImage.fromData(mutagen.mp3.MP3(self.FilePathList[0])['APIC:'].data).scaled(100, 100, Qt.KeepAspectRatio)))
				except:
					pass
		elif 2 <= len(self.FilePathList):
			self.setWindowTitle('{}, ...のプロパティ'.format(self.FilePathList[0].split('/')[-1]))
			self.FilePath.setText(list(set([QFileInfo(FilesPath).path() for FilesPath in self.FilePathList]))[0])
			FileFolderSize = '{}GB'.format(str(round(sum(QFileInfo(FilesSize).size() for FilesSize in self.FilePathList) / 1073741824, 2)))
			if FileFolderSize[0:2] == '0.':
				FileFolderSize = '{}MB'.format(str(round(sum(QFileInfo(FilesSize).size() for FilesSize in self.FilePathList) / 1048576, 2)))
				if FileFolderSize[0:2] == '0.':
					FileFolderSize = '{}KB'.format(str(round(sum(QFileInfo(FilesSize).size() for FilesSize in self.FilePathList) / 1024, 2)))
					if FileFolderSize[0:2] == '0.':
						FileFolderSize = '{}B'.format(str(round(sum(QFileInfo(FilesSize).size() for FilesSize in self.FilePathList), 2)))
						if FileFolderSize[0:2] == '0.':
							FileFolderSize = '不明なサイズ'
			self.FileSize.setText(FileFolderSize)
		self.FilesCount = 0
		self.FoldersCount = 0
		self.Files[0:] = []
		self.Folders[0:] = []

class EditCoverArtLabel(QLabel):
	def __init__(self, parent):
		super(EditCoverArtLabel, self).__init__(parent)
		self.setFixedSize(100, 100)
		self.setToolTip('<html><head/><body><p>アルバムカバー</p></body></html>')
		self.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.setContextMenuPolicy(Qt.CustomContextMenu)

	def CopyImage(self):
		with open('{}.jpg'.format('.'.join(EditFilePath[0].split('.')[0:-1])), 'wb') as CoverImage:
			if EditFilePath[0].lower().endswith('.flac'):
				CoverImage.write(mutagen.flac.FLAC(EditFilePath[0]).pictures[0].data)
			if EditFilePath[0].lower().endswith('.m4a'):
				CoverImage.write(mutagen.mp4.MP4(EditFilePath[0])['covr'][0])
			if EditFilePath[0].lower().endswith('.mp3'):
				CoverImage.write(mutagen.mp3.MP3(EditFilePath[0])['APIC:'].data)

	def mousePressEvent(self, event):
		self.CopyMenu = QMenu()
		self.CopyMenu.setStyleSheet('QMenu{background-color: #2d2d2d;color: #ededed;}'
									'QMenu::item:selected{background-color: #af0c00;color: #ededed;}')
		if event.type() == QEvent.MouseButtonPress and event.button() == Qt.RightButton:
			self.CopyMenu.addAction('カバーイメージを保存する', self.CopyImage)
			self.CopyMenu.exec(self.mapToGlobal(event.position().toPoint()))
		else:
			super(EditCoverArtLabel, self).mousePressEvent(event)

	def dragEnterEvent(self, event): # output
		if event.mimeData().hasUrls():
			event.accept()

	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.MoveAction)
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.setAccepted(True)
			event.accept()
			DropedCheck[0] = '1'
			for setCover in event.mimeData().urls():
				if os.path.isfile(str(setCover.toLocalFile())):
					DropedCoverImage[0] = open(str(setCover.toLocalFile()), 'rb').read()
					try:
						self.setPixmap(QPixmap(str(setCover.toLocalFile())).scaled(self.width(), self.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
					except:
						pass

class iconprovide(QFileIconProvider):
	def __init__(self):
		super(iconprovide, self).__init__()

	def icon(self, fileInfo):
		AcceptFileType = ('.svg', '.jpg', '.jpeg', '.png', '.bmp', '.gif', '.rgb', '.tiff', '.xbm', '.pbm', '.pgm', '.ppm')
		try:
			if fileInfo.isFile():
				if fileInfo.filePath().lower().endswith(AcceptFileType):
					return QIcon(LoadThread.submit(self.LoadImage, fileInfo.filePath()).result())
				if fileInfo.filePath().lower().endswith('.flac'):
					return QIcon(self.LoadFLAC(fileInfo.filePath()))
				if fileInfo.filePath().lower().endswith('.m4a'):
					return QIcon(self.LoadM4A(fileInfo.filePath()))
				if fileInfo.filePath().lower().endswith('.mp3'):
					return QIcon(self.LoadMP3(fileInfo.filePath()))
			return QFileIconProvider.icon(self, fileInfo)
		except:
			return QFileIconProvider.icon(self, fileInfo)

	def LoadImage(self, path):
		try:
			img = QPixmap(QSize(32, 32))
			img.load(path)
			return img
		except:
			pass

	def LoadFLAC(self, path):
		return QPixmap(QSize(64, 64)).fromImage(QImage.fromData(mutagen.flac.FLAC(path).pictures[0].data))

	def LoadMP3(self, path):
		return QPixmap(QSize(64, 64)).fromImage(QImage.fromData(mutagen.mp3.MP3(path)['APIC:'].data))

	def LoadM4A(self, path):
		return QPixmap(QSize(64, 64)).fromImage(QImage.fromData(mutagen.mp4.MP4(path)['covr'][0]))

class FileSystemListView(QListView):
	def __init__(self, parent, model=QFileSystemModel()):
		super().__init__(parent)
		self.Model = model
		self.setModel(self.Model)
		self.Model.setIconProvider(iconprovide())
		self.Model.setRootPath(os.path.expanduser("~"))
		try:
			self.setRootIndex(self.Model.index(os.path.expanduser("~")))
		except:
			self.setRootIndex(self.Model.index(os.path.expanduser("~")))
		self.setGeometry(QRect(276, 80, 545, 526))
		font1 = QFont()
		font1.setPointSize(50)
		self.setAutoScroll(False)
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setViewMode(QListView.ListMode)
		self.setIconSize(QSize(45, 45))
		self.setEditTriggers(QAbstractItemView.SelectedClicked)
		self.setContextMenuPolicy(Qt.CustomContextMenu)

	def index(self, path, column=0):
		return self.Model.index(path, column)

	def sort(self, column, order):
		self.Model.sort(column, order)

	def filePath(self, index):
		return self.Model.filePath(index)

	def rootPath(self):
		return self.Model.rootPath()

	def setRootPath(self, path):
		self.Model.setRootPath(path)

	def mousePressEvent(self, event):
		if not NowRootDirectoryPath[0] == '':
			self.RootPath = NowRootDirectoryPath[0]
		else:
			self.RootPath = os.path.expanduser('~')
		self.OutSideMenu = QMenu()
		self.OutSideMenu.setStyleSheet('QMenu{background-color: #2d2d2d;color: #ededed;} QMenu::item:selected{background-color: #af0c00;color: #ededed;}')
		self.OutSideMenu.setMaximumHeight(480)
		if event.type() == QEvent.MouseButtonPress:
			if event.button() == Qt.RightButton:
				try:
					for LoopIndex, FileFolderIndex in enumerate(self.selectedIndexes()):
						if os.path.isfile(self.filePath(FileFolderIndex)) and not os.path.islink(self.filePath(FileFolderIndex)) and LoopIndex == 0:
							self.OutSideMenu.addAction('ファイルを開く', self.OutSideOpenFile)
							self.OutSideMenu.addAction('名前の変更', self.OutSideRenames)
						if not os.path.isfile(self.filePath(FileFolderIndex)) and not os.path.islink(self.filePath(FileFolderIndex)) and LoopIndex == 0:
							self.OutSideMenu.addAction('名前の変更', self.OutSideRenames)
							self.OutSideMenu.addAction('フォルダを開く', self.OutSideOpenFile)
						if os.path.isfile(self.filePath(FileFolderIndex)) and not os.path.islink(self.filePath(FileFolderIndex)) and LoopIndex == 0:
							if event.modifiers() == Qt.ShiftModifier:
								self.OutSideMenu.addAction('完全削除', self.OutSideForceDeleting)
							else:
								self.OutSideMenu.addAction('削除', self.OutSideDeleting)
							self.OutSideMenu.addAction('コピー', self.OutSideCopyFile)
							self.OutSideMenu.addAction('移動', self.OutSideCopyFile)
						if os.path.isfile(self.filePath(FileFolderIndex)) and LoopIndex == 0 and self.filePath(FileFolderIndex).endswith('.zip') or self.filePath(FileFolderIndex).endswith('.tar.gz') or self.filePath(FileFolderIndex).endswith('.7z'):
							self.OutSideMenu.addAction('解凍', self.OutSideUnArchive)
						if not os.path.isfile(self.filePath(FileFolderIndex)) and not os.path.islink(self.filePath(FileFolderIndex)) and LoopIndex == 0:
							if event.modifiers() == Qt.ShiftModifier:
								self.OutSideMenu.addAction('完全削除', self.OutSideForceDeleting)
							else:
								self.OutSideMenu.addAction('削除', self.OutSideDeleting)
							self.OutSideMenu.addAction('フォルダのコピー', self.OutSideCopyFile)
							self.OutSideMenu.addAction('フォルダの移動', self.OutSideCopyFile)
					try:
						if os.path.isfile(self.filePath(self.selectedIndexes()[0])) or os.path.isdir(self.filePath(self.selectedIndexes()[0])):
							self.SendMenu = self.OutSideMenu.addMenu('送る')
							self.SendMenu.setStyleSheet('QMenu{background-color: #2d2d2d;color: #ededed;} QMenu::item:selected{background-color: #af0c00;color: #ededed;}')
							self.SendMenu.addAction('圧縮', self.OutSideArchiveCreate)
					except:
						pass
					self.OutSideMenu.addAction('現在の場所を開く', self.OutSideNowOpenFolder)
					self.OutSideMenu.addAction('現在のフォルダパスをコピー', self.OutSideCopiedPath)
					self.OutSideMenu.addAction('フォルダの新規作成', self.OutSideCreateFolder)
					self.OutSideMenu.addAction('新しいファイルを作成', self.OutSideCreateNewFile)
					if not CopiedItems[0] == '':
						self.OutSideMenu.addAction('ここにファイルをコピー', self.OutSideCopiedFiles)
						self.OutSideMenu.addAction('ここにファイルを移動', self.OutSideMovedFile)
					self.OutSideMenu.addAction('プロパティを見る', self.OutSidePropaty)
					self.OutSideMenu.exec(self.mapToGlobal(event.position().toPoint()))
				except:
					pass
				super(FileSystemListView, self).mousePressEvent(event)
			else:
				super(FileSystemListView, self).mousePressEvent(event)
		else:
			SelectedItem[0] = '0'
			super(FileSystemListView, self).mousePressEvent(event)

	def OutSidePropaty(self):
		for p in self.selectedIndexes():
			EditFilePath.append(self.filePath(p))
		if len(self.selectedIndexes()) == 0:
			EditFilePath.append(self.rootPath())
		PropertyDiaLog = EditMusicTagDailog(EditFilePath)
		PropertyDiaLog.exec()
		if PropertyDiaLog.result() == QDialog.Accepted:
			if len(EditFilePath) == 1:
				if EditFilePath[0].lower().endswith('.flac'):
					FlacData = mutagen.flac.FLAC(EditFilePath[0])
					try:
						FlacData.tags['title'] = PropertyDiaLog.TrackName.text()
					except:
						pass
					try:
						FlacData.tags['artist'] = PropertyDiaLog.TrackArtist.text()
					except:
						pass
					try:
						FlacData.tags['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
					except:
						pass
					try:
						FlacData.tags['album'] = PropertyDiaLog.TrackAlbum.text()
					except:
						pass
					try:
						FlacData.tags['genre'] = PropertyDiaLog.TrackGenre.text()
					except:
						pass
					try:
						FlacData.tags['date'] = PropertyDiaLog.TrackYear.text()
					except:
						pass
					try:
						FlacData.tags['tracknumber'] = PropertyDiaLog.TrackNum.text()
					except:
						pass
					try:
						if PropertyDiaLog.TrackDiscNum.text() == '':
							FlacData.tags['discnumber'] = '0'
						elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
							if not '/' in PropertyDiaLog.TrackDiscNum.text():
								FlacData.tags['discnumber'] = [('0', PropertyDiaLog.TrackDiscNum.text())]
							else:
								FlacData.tags['discnumber'] = [(PropertyDiaLog.TrackDiscNum.text().split('/')[0], PropertyDiaLog.TrackDiscNum.text().split()[1])]
						else:
							FlacData.tags['discnumber'] = [(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0], PropertyDiaLog.TrackDiscNum.text().split(' / ')[1])]
					except:
						pass
					try:
						cover_picture = mutagen.flac.Picture()
						cover_picture.data = bytes(DropedCoverImage[0])
						FlacData.clear_pictures()
						FlacData.add_picture(cover_picture)
					except:
						pass
					FlacData.save()
				if EditFilePath[0].lower().endswith('.m4a'):
					M4AData = mutagen.mp4.MP4(EditFilePath[0])
					try:
						M4AData.tags['\xa9nam'] = PropertyDiaLog.TrackName.text()
					except:
						pass
					try:
						M4AData.tags['\xa9ART'] = PropertyDiaLog.TrackArtist.text()
					except:
						pass
					try:
						M4AData.tags['aART'] = PropertyDiaLog.TrackAlbumArtist.text()
					except:
						pass
					try:
						M4AData.tags['\xa9alb'] = PropertyDiaLog.TrackAlbum.text()
					except:
						pass
					try:
						M4AData.tags['\xa9gen'] = PropertyDiaLog.TrackGenre.text()
					except:
						pass
					try:
						M4AData.tags['\xa9day'] = PropertyDiaLog.TrackYear.text()
					except:
						pass
					try:
						if PropertyDiaLog.TrackNum.text() == '':
							M4AData.tags['trkn'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackNum.text():
							if not '/' in PropertyDiaLog.TrackNum.text():
								M4AData.tags['trkn'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
							else:
								M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]), int(PropertyDiaLog.TrackNum.text().split()[1]))]
						else:
							M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						if PropertyDiaLog.TrackDiscNum.text() == '':
							M4AData.tags['disk'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
							if not '/' in PropertyDiaLog.TrackDiscNum.text():
								M4AData.tags['disk'] = [(0, PropertyDiaLog.TrackDiscNum.text())]
							else:
								M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]), int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
						else:
							M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						M4AData.tags['covr'] = [bytes(DropedCoverImage[0])]
					except:
						pass
					M4AData.save()
				if EditFilePath[0].lower().endswith('.mp3'):
					MP3Data = EasyID3(EditFilePath[0])
					setCoverMP3 = mutagen.id3.ID3(EditFilePath[0])
					try:
						MP3Data['title'] = PropertyDiaLog.TrackName.text()
					except:
						pass
					try:
						MP3Data['artist'] = PropertyDiaLog.TrackArtist.text()
					except:
						pass
					try:
						MP3Data['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
					except:
						pass
					try:
						MP3Data['album'] = PropertyDiaLog.TrackAlbum.text()
					except:
						pass
					try:
						MP3Data['genre'] = PropertyDiaLog.TrackGenre.text()
					except:
						pass
					try:
						MP3Data['data'] = PropertyDiaLog.TrackYear.text()
					except:
						pass
					try:
						if PropertyDiaLog.TrackNum.text() == '':
							MP3Data['tracknumber'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackNum.text():
							if not '/' in PropertyDiaLog.TrackNum.text():
								MP3Data['tracknumber'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
							else:
								MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]), int(PropertyDiaLog.TrackNum.text().split()[1]))]
						else:
							MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						if PropertyDiaLog.TrackDiscNum.text() == '':
							MP3Data['discnumber'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
							if not '/' in PropertyDiaLog.TrackDiscNum.text():
								MP3Data['discnumber'] = [(0, int(PropertyDiaLog.TrackDiscNum.text()))]
							else:
								MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]), int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
						else:
							MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						setCoverMP3['APIC:'].data = bytes(DropedCoverImage[0])
					except:
						pass
					MP3Data.save()
					setCoverMP3.save()
			elif 2 <= len(EditFilePath):
				if not len(EditMediaPath_FLAC) == 0:
					for FlacFilePath in EditMediaPath_FLAC:
						FLACData = mutagen.flac.FLAC(FlacFilePath)
						if not PropertyDiaLog.TrackName.text() == '(複数の値)':
							try:
								FLACData.tags['title'] = PropertyDiaLog.TrackName.text()
							except:
								pass
						if not PropertyDiaLog.TrackArtist.text() == '(複数の値)':
							try:
								FLACData.tags['artist'] = PropertyDiaLog.TrackArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbumArtist.text() == '(複数の値)':
							try:
								FLACData.tags['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbum.text() == '(複数の値)':
							try:
								FLACData.tags['album'] = PropertyDiaLog.TrackAlbum.text()
							except:
								pass
						if not PropertyDiaLog.TrackGenre.text() == '(複数の値)':
							try:
								FLACData.tags['genre'] = PropertyDiaLog.TrackGenre.text()
							except:
								pass
						if not PropertyDiaLog.TrackYear.text() == '(複数の値)':
							try:
								FLACData.tags['date'] = PropertyDiaLog.TrackYear.text()
							except:
								pass
						if not PropertyDiaLog.TrackNum.text() == '(複数の値)':
							try:
								FLACData.tags['tracknumber'] = PropertyDiaLog.TrackNum.text()
							except:
								pass
						if DropedCheck[0] == '1':
							try:
								cover_picture = mutagen.flac.Picture()
								cover_picture.data = bytes(DropedCoverImage[0])
								FLACData.clear_pictures()
								FLACData.add_picture(cover_picture)
							except:
								pass
							pass
						FLACData.save()
				if not len(EditMediaPath_M4A) == 0:
					for M4AFilePath in EditMediaPath_M4A:
						M4AData = mutagen.mp4.MP4(M4AFilePath)
						if not PropertyDiaLog.TrackName.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9nam'] = PropertyDiaLog.TrackName.text()
							except:
								pass
						if not PropertyDiaLog.TrackArtist.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9ART'] = PropertyDiaLog.TrackArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbumArtist.text() == '(複数の値)':
							try:
								M4AData.tags['aART'] = PropertyDiaLog.TrackAlbumArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbum.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9alb'] = PropertyDiaLog.TrackAlbum.text()
							except:
								pass
						if not PropertyDiaLog.TrackGenre.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9gen'] = PropertyDiaLog.TrackGenre.text()
							except:
								pass
						if not PropertyDiaLog.TrackYear.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9day'] = PropertyDiaLog.TrackYear.text()
							except:
								pass
						if not PropertyDiaLog.TrackNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackNum.text() == '':
									M4AData.tags['trkn'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackNum.text():
									if not '/' in PropertyDiaLog.TrackNum.text():
										M4AData.tags['trkn'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
									else:
										M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]),
																 int(PropertyDiaLog.TrackNum.text().split()[1]))]
								else:
									M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]),
															 int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
							except:
								pass
						if not PropertyDiaLog.TrackDiscNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackDiscNum.text() == '':
									M4AData.tags['disk'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
									if not '/' in PropertyDiaLog.TrackDiscNum.text():
										M4AData.tags['disk'] = [(0, PropertyDiaLog.TrackDiscNum.text())]
									else:
										M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]),
																 int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
								else:
									M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]),
															 int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
							except:
								pass
						if DropedCheck[0] == '1':
							try:
								M4AData.tags['covr'] = [bytes(DropedCoverImage[0])]
							except:
								pass
						M4AData.save()
				if not len(EditMediaPath_MP3) == 0:
					for MP3FilePath in EditMediaPath_MP3:
						MP3Data = EasyID3(MP3FilePath)
						setCoverMP3 = mutagen.id3.ID3(MP3FilePath)
						if not PropertyDiaLog.TrackName.text() == '(複数の値)':
							try:
								MP3Data['title'] = PropertyDiaLog.TrackName.text()
							except:
								pass
						if not PropertyDiaLog.TrackArtist.text() == '(複数の値)':
							try:
								MP3Data['artist'] = PropertyDiaLog.TrackArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbumArtist.text() == '(複数の値)':
							try:
								MP3Data['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbum.text()  == '(複数の値)':
							try:
								MP3Data['album'] = PropertyDiaLog.TrackAlbum.text()
							except:
								pass
						if not PropertyDiaLog.TrackGenre.text() == '(複数の値)':
							try:
								MP3Data['genre'] = PropertyDiaLog.TrackGenre.text()
							except:
								pass
						if not PropertyDiaLog.TrackYear.text() == '(複数の値)':
							try:
								MP3Data['data'] = PropertyDiaLog.TrackYear.text()
							except:
								pass
						if not PropertyDiaLog.TrackNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackNum.text() == '':
									MP3Data['tracknumber'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackNum.text():
									if not '/' in PropertyDiaLog.TrackNum.text():
										MP3Data['tracknumber'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
									else:
										MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]),
																   int(PropertyDiaLog.TrackNum.text().split()[1]))]
								else:
									MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]),
															   int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
							except:
								pass
						if not PropertyDiaLog.TrackDiscNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackDiscNum.text() == '':
									MP3Data['discnumber'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
									if not '/' in PropertyDiaLog.TrackDiscNum.text():
										MP3Data['discnumber'] = [(0, int(PropertyDiaLog.TrackDiscNum.text()))]
									else:
										MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]),
																  int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
								else:
									MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]),
															  int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
							except:
								pass
						if DropedCheck[0] == '1':
							try:
								setCoverMP3['APIC:'].data = bytes(DropedCoverImage[0])
							except:
								pass
						MP3Data.save()
						setCoverMP3.save()
		DropedCheck[0] = '0'
		EditFilePath[0:] = []

	def OutSideCopiedPath(self):
		QApplication.clipboard().setText(self.rootPath())

	def OutSideForceDeleting(self):
		Result = ForceDeletingOKDialog.OutPutResult()
		try:
			if Result == '0':
				for ForceRemove in self.selectedIndexes():
					if os.path.isfile(self.filePath(ForceRemove)):
						os.remove(self.filePath(ForceRemove))
					else:
						shutil.rmtree(self.filePath(ForceRemove))
		except:
			pass

	def OutSideDeleting(self):
		Result = DeletingOKDialog.OutPutResult()
		try:
			if Result == '0':
				for RemoveItem in self.selectedIndexes():
					send2trash.send2trash(self.filePath(RemoveItem))
		except:
			pass

	def OutSideRenames(self):
		SelectedItemPath[0] = self.filePath(self.selectedIndexes()[0]).split('/')[-1]
		Result = InputDiaLog.OutputResult()
		if Result[1] == '0':
			if not Result[0] == '':
				if not Result[0] == ' ':
					text = Result[0]
					oldname = self.filePath(self.selectedIndexes()[0])
					newName = '{}{}'.format(oldname.split(oldname.split('/')[-1])[0], text)
					try:
						os.rename(oldname, newName)
					except:
						pass

	def OutSideOpenFile(self):
		for SelectedIndex in self.selectedIndexes():
			QDesktopServices.openUrl('file:///{}'.format(self.filePath(SelectedIndex)))

	def OutSideNowOpenFolder(self):
		if not NowRootDirectoryPath[0] == '':
			self.RootPath = NowRootDirectoryPath[0]
		else:
			self.RootPath = os.path.expanduser('~')
		QDesktopServices.openUrl('file:///{}'.format(self.RootPath))

	def OutSideCreateFolder(self):
		if not NowRootDirectoryPath[0] == '':
			self.RootPath = NowRootDirectoryPath[0]
		else:
			self.RootPath = os.path.expanduser('~')
		Result = NewCreateFolderDialog.OutputResult()
		if Result[1] == '0':
			if not Result[0] == '':
				if not Result[0] == ' ':
					try:
						os.mkdir('{}{}{}'.format(self.RootPath, '/', Result[0]))
					except:
						for c in range(9999):
							try:
								os.mkdir('{}{}{} ({})'.format(self.RootPath, '/', Result[0], c))
								break
							except:
								pass

	def OutSideCreateNewFile(self):
		if not NowRootDirectoryPath[0] == '':
			self.RootPath = NowRootDirectoryPath[0]
		else:
			self.RootPath = os.path.expanduser('~')
		Results = NewFileCreateDialog.OutputResults()
		if Results[1] == '0':
			if not Results[0] == '':
				if not Results[0] == ' ':
					with open('{}{}{}'.format(self.RootPath, '/', Results[0]), 'w', encoding='utf-8') as NewFile:
						NewFile.write('')

	def OutSideMovedFile(self):
		if not NowRootDirectoryPath[0] == '':
			self.RootPath = NowRootDirectoryPath[0]
		else:
			self.RootPath = os.path.expanduser('~')
		if CopiedItemCount[0] == len(CopiedItems[0]):
			for MoveItem in CopiedItems[0]:
				try:
					shutil.move(MoveItem, self.RootPath)
				except:
					pass

	def OutSideCopyFile(self):
		CopiedItems[0] = [self.filePath(countItem) for countItem in self.selectedIndexes()]
		CopiedItemCount[0] = len(self.selectedIndexes())

	def OutSideCopiedFiles(self):
		if not NowRootDirectoryPath[0] == '':
			self.RootPath = NowRootDirectoryPath[0]
		else:
			self.RootPath = os.path.expanduser('~')
		if CopiedItemCount[0] == len(CopiedItems[0]):
			for CopiedItem in CopiedItems[0]:
				newPath = '{}{}{}'.format(self.RootPath, '/', CopiedItem.split('/')[-1])
				if not QFile.exists(newPath):
					if os.path.isfile(CopiedItem):
						print(newPath)
						shutil.copyfile(CopiedItem, newPath)
					elif os.path.isdir(CopiedItem) and not os.path.islink(CopiedItem):
						shutil.copytree(CopiedItem, newPath)
				else:
					for cc in range(9999):
						print()
						if not QFile.exists('{} ({}).{}'.format('.'.join(newPath.split('.')[0:-1]), cc+1, newPath.split('.')[-1])):
							if os.path.isfile(CopiedItem):
								shutil.copyfile(CopiedItem, '{} ({}).{}'.format('.'.join(newPath.split('.')[0:-1]), cc+1, newPath.split('.')[-1]))
							elif os.path.isdir(CopiedItem) and not os.path.islink(CopiedItem):
								shutil.copytree(CopiedItem, '{} ({}).{}'.format('.'.join(newPath.split('.')[0:-1]), cc+1, newPath.split('.')[-1]))
							break
						else:
							pass

	def OutSideArchiveCreate(self):
		BackupNowPath[0] = os.getcwd()
		Result = ArchiveDialog.OutPutResult()
		FileName = Result[0]
		mode = Result[1]
		CheckOK = Result[2]
		if not CheckOK == '':
			if mode == 'ZipArchive':
				os.chdir(self.rootPath())
				with zipfile.ZipFile(FileName, 'w') as ZF:
					for ArchiveDFile in self.selectedIndexes():
						if os.path.isfile(self.filePath(ArchiveDFile)):
							ZF.write(self.filePath(ArchiveDFile).split('/')[-1])
						elif os.path.isdir(self.filePath(ArchiveDFile)):
							for TargetFolder, __, TargetFile in os.walk(self.filePath(ArchiveDFile)):
								for TFile in TargetFile:
									if not TFile.startswith('.'):
										FilePaths = os.path.join(TargetFolder, TFile).replace(os.getcwd(), os.curdir)
										ZF.write(FilePaths)
				os.chdir(BackupNowPath[0])
			if mode == 'TarArchive':
				os.chdir(self.rootPath())
				with tarfile.open(FileName, 'w:gz') as Tgz:
					for TarAddFiles in self.selectedIndexes():
						Tgz.add(self.filePath(TarAddFiles).replace(os.getcwd(), os.curdir))
				os.chdir(BackupNowPath[0])
			if mode == '7ZipArchive':
				os.chdir(self.rootPath())
				with py7zr.SevenZipFile(FileName, 'w') as SevenZipper:
					for SevenFilesIndex in self.selectedIndexes():
						SevenZipper.writeall(self.filePath(SevenFilesIndex).replace(os.getcwd(), os.curdir))
				os.chdir(BackupNowPath[0])

	def OutSideUnArchive(self):
		BackupNowPath[0] = os.getcwd()
		os.chdir(self.rootPath())
		for DetectFile in self.selectedIndexes():
			if self.filePath(DetectFile).endswith('.zip'):
				os.makedirs(self.filePath(DetectFile).replace(os.getcwd(), os.curdir).split('.zip')[0], exist_ok=True)
				with zipfile.ZipFile(self.filePath(DetectFile), 'r') as ExtractZip:
					ExtractZip.extractall(path='{}{}{}'.format(os.getcwd(), '/', self.filePath(DetectFile).split(os.getcwd())[-1].split('.zip')[0]))
			if self.filePath(DetectFile).endswith('.tar.gz'):
				os.makedirs(self.filePath(DetectFile).replace(os.getcwd(), os.curdir).split('.tar.gz')[0], exist_ok=True)
				with tarfile.open(self.filePath(DetectFile), 'r') as ExtractTgz:
	def is_within_directory(directory, target):
		
		abs_directory = os.path.abspath(directory)
		abs_target = os.path.abspath(target)
	
		prefix = os.path.commonprefix([abs_directory, abs_target])
		
		return prefix == abs_directory
	
	def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
	
		for member in tar.getmembers():
			member_path = os.path.join(path, member.name)
			if not is_within_directory(path, member_path):
				raise Exception("Attempted Path Traversal in Tar File")
	
		tar.extractall(path, members, numeric_owner) 
		
	
	safe_extract(ExtractTgz, path="{}{}{}".format(os.getcwd(),"/",self.filePath(DetectFile).split(os.getcwd())[-"1"].split(".tar.gz")["0"]))
			if self.filePath(DetectFile).endswith('.7z'):
				os.makedirs(self.filePath(DetectFile).replace(os.getcwd(), os.curdir).split('.7z')[0], exist_ok=True)
				with py7zr.SevenZipFile(self.filePath(DetectFile), 'r') as ExtractSevenZip:
					ExtractSevenZip.extractall(path='{}{}{}'.format(os.getcwd(), '/', self.filePath(DetectFile).split(os.getcwd())[-1].split('.7z')[0]))
		os.chdir(BackupNowPath[0])

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
			for ff in event.mimeData().urls():
				newpath = '{}{}{}'.format(self.rootPath(), '/', str(ff.toLocalFile()).split('/')[-1])
				try:
					if os.path.isfile(str(ff.toLocalFile())):
							shutil.move(str(ff.toLocalFile()), newpath)
					else:
						shutil.move(str(ff.toLocalFile()), newpath)
				except:
					pass
		else:
			event.ignore()

	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.setAccepted(True)
			event.accept()
			for c in event.mimeData().urls():
				newpath = '{}{}{}'.format(self.rootPath(), '/', str(c.toLocalFile()).split('/')[-1])
				try:
					if os.path.isfile(str(c.toLocalFile())):
							shutil.move(str(c.toLocalFile()), newpath)
					else:
						shutil.move(str(c.toLocalFile()), newpath)
				except:
					pass
		else:
			event.ignore()

class ArchiveDialog(QDialog):
	def __init__(self):
		super(ArchiveDialog, self).__init__()
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.setWindowTitle('圧縮ファイルの作成')
		self.setFixedSize(500, 130)
		self.NoneLabel = QLabel('\t', self)
		self.NoneLabel2 = QLabel('\t\t\t\t\t\t', self)
		self.NoneLabel3 = QLabel('\t', self)
		self.ArchiveLabel1 = QLabel('圧縮ファイル名: ', self)
		self.ArchiveLabel1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.ArchiveInput = QLineEdit()
		self.ArchiveInput.setText('Archive.zip')
		self.ArchiveInput.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
		self.ArchiveInput.setClearButtonEnabled(True)
		self.ArchiveType1 = QCheckBox()
		self.ArchiveType1.setStyleSheet('QCheckBox{background-color: #2d2d2d;color: #ededed;}')
		self.ArchiveType1.setChecked(True)
		self.ArchiveType1.setText('.zip')
		self.ArchiveType1.setStyleSheet('QCheckBox{background-color: #2d2d2d;color: #ededed;}')
		self.ArchiveType2 = QCheckBox()
		self.ArchiveType2.setChecked(False)
		self.ArchiveType2.setText('.tar.gz')
		self.ArchiveType2.setStyleSheet('QCheckBox{background-color: #2d2d2d;color: #ededed;}')
		self.ArchiveType3 = QCheckBox()
		self.ArchiveType3.setChecked(False)
		self.ArchiveType3.setText('.7z')
		self.ArchiveType3.setStyleSheet('QCheckBox{background-color: #2d2d2d;color: #ededed;}')
		self.selectorButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.selectorButton.rejected.connect(self.reject)
		self.selectorButton.accepted.connect(self.accept)
		self.selectorButton.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.Popup = QGridLayout() # row = 縦, column = 横
		self.Popup.addWidget(self.ArchiveLabel1, 0, 0)
		self.Popup.addWidget(self.ArchiveInput, 0, 1)
		self.Popup.addWidget(self.ArchiveType1, 1, 0)
		self.Popup.addWidget(self.ArchiveType2, 1, 1)
		self.Popup.addWidget(self.ArchiveType3, 1, 2)
		self.Popup.addWidget(self.selectorButton, 1, 4)
		self.Popup.addWidget(self.NoneLabel, 2, 0)
		self.Popup.addWidget(self.NoneLabel2, 2, 1)
		self.Popup.addWidget(self.NoneLabel3, 2, 2)
		self.setLayout(self.Popup)
		self.ArchiveType1.stateChanged.connect(self.CheckModes)
		self.ArchiveType2.stateChanged.connect(self.CheckModes)
		self.ArchiveType3.stateChanged.connect(self.CheckModes)

	def CheckModes(self):
		try:
			if self.ArchiveType1.checkState() == Qt.Unchecked and OneChecked[0] == '1':
				self.ArchiveType1.setCheckState(Qt.Checked)
			if self.ArchiveType2.checkState() == Qt.Unchecked and OneChecked2[0] == '1':
				self.ArchiveType2.setCheckState(Qt.Checked)
			if self.ArchiveType3.checkState() == Qt.Unchecked and OneChecked3[0] == '1':
				self.ArchiveType3.setCheckState(Qt.Checked)
			if self.ArchiveType1.checkState() == Qt.Checked and OneChecked2[0] == '1':
				self.ArchiveType2.setCheckState(Qt.Unchecked)
				OneChecked2[0] = '0'
				OneChecked[0] = '1'
			if self.ArchiveType1.checkState() == Qt.Checked and OneChecked3[0] == '1':
				self.ArchiveType3.setCheckState(Qt.Unchecked)
				OneChecked3[0] = '0'
				OneChecked[0] = '1'
			if self.ArchiveType2.checkState() == Qt.Checked and OneChecked[0] == '1':
				self.ArchiveType1.setCheckState(Qt.Unchecked)
				OneChecked[0] = '0'
				OneChecked2[0] = '1'
			if self.ArchiveType3.checkState() == Qt.Checked and OneChecked[0] == '1':
				self.ArchiveType1.setCheckState(Qt.Unchecked)
				OneChecked[0] = '0'
				OneChecked3[0] = '1'
			if self.ArchiveType1.checkState() == Qt.Checked and OneChecked2[0] == '1':
				self.ArchiveType2.setCheckState(Qt.Unchecked)
				OneChecked2[0] = '0'
				OneChecked[0] = '1'
			if self.ArchiveType3.checkState() == Qt.Checked and OneChecked2[0] == '1':
				self.ArchiveType2.setCheckState(Qt.Unchecked)
				OneChecked2[0] = '0'
				OneChecked3[0] = '1'
			if self.ArchiveType1.checkState() == Qt.Checked and OneChecked3[0] == '1':
				self.ArchiveType3.setCheckState(Qt.Unchecked)
				OneChecked3[0] = '0'
				OneChecked[0] = '1'
			if self.ArchiveType2.checkState() == Qt.Checked and OneChecked3[0] == '1':
				self.ArchiveType3.setCheckState(Qt.Unchecked)
				OneChecked3[0] = '0'
				OneChecked[0] = '1'
			if self.ArchiveType3.checkState() == Qt.Checked:
				if not self.ArchiveInput.text() == '':
					self.ArchiveInput.setText(self.ArchiveInput.text().replace(self.ArchiveInput.text().split('.')[-1], '7z').replace('.tar', ''))
				else:
					self.ArchiveInput.setText('Archive.7z')
				OneChecked3[0] = '1'
			if self.ArchiveType2.checkState() == Qt.Checked:
				if not self.ArchiveInput.text() == '':
					if self.ArchiveInput.text().split('.')[-1] == 'zip' or self.ArchiveInput.text().split('.')[-1] == '7z':
						self.ArchiveInput.setText(self.ArchiveInput.text().replace(self.ArchiveInput.text().split('.')[-1], 'tar.gz').replace('.tar.tar', ''))
				else:
					self.ArchiveInput.setText('Archive.tar.gz')
				OneChecked2[0] = '1'
			if self.ArchiveType1.checkState() == Qt.Checked:
				if not self.ArchiveInput.text() == '':
					self.ArchiveInput.setText(self.ArchiveInput.text().replace(self.ArchiveInput.text().split('.')[-1], 'zip').replace('.tar', ''))
				else:
					self.ArchiveInput.setText('Archive.zip')
				OneChecked[0] = '1'
		except:
			pass

	def InputResult(self):
		return self.ArchiveInput.text()

	def ModeCheck(self):
		if self.ArchiveType1.checkState() == Qt.Checked:
			return 'ZipArchive'
		elif self.ArchiveType2.checkState() == Qt.Checked:
			return 'TarArchive'
		elif self.ArchiveType3.checkState() == Qt.Checked:
			return '7ZipArchive'

	@staticmethod
	def OutPutResult():
		Ac = ArchiveDialog()
		Ac.exec()
		inputFileName = Ac.InputResult()
		mode = Ac.ModeCheck()
		if Ac.result() == QDialog.Accepted:
			return inputFileName, mode, '0'
		elif Ac.result() == QDialog.Rejected:
			return '', '', ''

class SearchWindow(QWidget):
	def __init__(self, parent=None, model=None):
		super(SearchWindow, self).__init__(parent)
		self.w = QDialog(parent)
		self.w.resize(QSize(1000, 700))
		self.w.setFixedSize(QSize(1000, 700))
		self.w.setWindowTitle('検索結果')
		self.w.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.ListView = QListView()
		self.ListView.setStyleSheet('QListView{background-color: #2d2d2d;color: #ededed;}')
		self.ListView.setGeometry(QRect(-1, -1, 800, 638))
		self.ListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ListView.setContextMenuPolicy(Qt.CustomContextMenu)
		self.ListView.customContextMenuRequested.connect(self.CopyOnlyMenu)
		self.Model = model
		self.ListView.setModel(self.Model)
		self.ListView.doubleClicked.connect(self.mouseDoubleClicked)
		self.LayOut = QGridLayout()
		self.LayOut.addWidget(self.ListView, 0, 0)
		self.w.setLayout(self.LayOut)

	def CopyOnlyMenu(self, Point):
		self.CopyMenu = QMenu()
		self.CopyMenu.setStyleSheet('QMenu{background-color: #2d2d2d;color: #ededed;} QMenu::item:selected{background-color: #af0c00;color: #ededed;}')
		self.CopyMenu.addAction('場所のコピー', self.CopyPath)
		self.CopyMenu.addAction('プロパティ', self.PropertyMenu)
		self.CopyMenu.exec(self.ListView.mapToGlobal(Point))

	def PropertyMenu(self):
		for p in self.ListView.selectedIndexes():
			EditFilePath.append(p.data())
		if len(self.ListView.selectedIndexes()) == 0:
			EditFilePath.append(NowRootDirectoryPath[0])
		PropertyDiaLog = EditMusicTagDailog(EditFilePath)
		PropertyDiaLog.exec()
		if PropertyDiaLog.result() == QDialog.Accepted:
			if len(EditFilePath) == 1:
				if EditFilePath[0].lower().endswith('.flac'):
					FlacData = mutagen.flac.FLAC(EditFilePath[0])
					try:
						FlacData.tags['title'] = PropertyDiaLog.TrackName.text()
					except:
						pass
					try:
						FlacData.tags['artist'] = PropertyDiaLog.TrackArtist.text()
					except:
						pass
					try:
						FlacData.tags['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
					except:
						pass
					try:
						FlacData.tags['album'] = PropertyDiaLog.TrackAlbum.text()
					except:
						pass
					try:
						FlacData.tags['genre'] = PropertyDiaLog.TrackGenre.text()
					except:
						pass
					try:
						FlacData.tags['date'] = PropertyDiaLog.TrackYear.text()
					except:
						pass
					try:
						FlacData.tags['tracknumber'] = PropertyDiaLog.TrackNum.text()
					except:
						pass
					try:
						if PropertyDiaLog.TrackDiscNum.text() == '':
							FlacData.tags['discnumber'] = '0'
						elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
							if not '/' in PropertyDiaLog.TrackDiscNum.text():
								FlacData.tags['discnumber'] = [('0', PropertyDiaLog.TrackDiscNum.text())]
							else:
								FlacData.tags['discnumber'] = [(PropertyDiaLog.TrackDiscNum.text().split('/')[0], PropertyDiaLog.TrackDiscNum.text().split()[1])]
						else:
							FlacData.tags['discnumber'] = [(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0], PropertyDiaLog.TrackDiscNum.text().split(' / ')[1])]
					except:
						pass
					try:
						cover_picture = mutagen.flac.Picture()
						cover_picture.data = bytes(DropedCoverImage[0])
						FlacData.clear_pictures()
						FlacData.add_picture(cover_picture)
					except:
						pass
					FlacData.save()
				if EditFilePath[0].lower().endswith('.m4a'):
					M4AData = mutagen.mp4.MP4(EditFilePath[0])
					try:
						M4AData.tags['\xa9nam'] = PropertyDiaLog.TrackName.text()
					except:
						pass
					try:
						M4AData.tags['\xa9ART'] = PropertyDiaLog.TrackArtist.text()
					except:
						pass
					try:
						M4AData.tags['aART'] = PropertyDiaLog.TrackAlbumArtist.text()
					except:
						pass
					try:
						M4AData.tags['\xa9alb'] = PropertyDiaLog.TrackAlbum.text()
					except:
						pass
					try:
						M4AData.tags['\xa9gen'] = PropertyDiaLog.TrackGenre.text()
					except:
						pass
					try:
						M4AData.tags['\xa9day'] = PropertyDiaLog.TrackYear.text()
					except:
						pass
					try:
						if PropertyDiaLog.TrackNum.text() == '':
							M4AData.tags['trkn'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackNum.text():
							if not '/' in PropertyDiaLog.TrackNum.text():
								M4AData.tags['trkn'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
							else:
								M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]), int(PropertyDiaLog.TrackNum.text().split()[1]))]
						else:
							M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						if PropertyDiaLog.TrackDiscNum.text() == '':
							M4AData.tags['disk'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
							if not '/' in PropertyDiaLog.TrackDiscNum.text():
								M4AData.tags['disk'] = [(0, PropertyDiaLog.TrackDiscNum.text())]
							else:
								M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]), int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
						else:
							M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						M4AData.tags['covr'] = [bytes(DropedCoverImage[0])]
					except:
						pass
					M4AData.save()
				if EditFilePath[0].lower().endswith('.mp3'):
					MP3Data = EasyID3(EditFilePath[0])
					setCoverMP3 = mutagen.id3.ID3(EditFilePath[0])
					try:
						MP3Data['title'] = PropertyDiaLog.TrackName.text()
					except:
						pass
					try:
						MP3Data['artist'] = PropertyDiaLog.TrackArtist.text()
					except:
						pass
					try:
						MP3Data['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
					except:
						pass
					try:
						MP3Data['album'] = PropertyDiaLog.TrackAlbum.text()
					except:
						pass
					try:
						MP3Data['genre'] = PropertyDiaLog.TrackGenre.text()
					except:
						pass
					try:
						MP3Data['data'] = PropertyDiaLog.TrackYear.text()
					except:
						pass
					try:
						if PropertyDiaLog.TrackNum.text() == '':
							MP3Data['tracknumber'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackNum.text():
							if not '/' in PropertyDiaLog.TrackNum.text():
								MP3Data['tracknumber'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
							else:
								MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]), int(PropertyDiaLog.TrackNum.text().split()[1]))]
						else:
							MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						if PropertyDiaLog.TrackDiscNum.text() == '':
							MP3Data['discnumber'] = [(0, 0)]
						elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
							if not '/' in PropertyDiaLog.TrackDiscNum.text():
								MP3Data['discnumber'] = [(0, int(PropertyDiaLog.TrackDiscNum.text()))]
							else:
								MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]), int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
						else:
							MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
					except:
						pass
					try:
						setCoverMP3['APIC:'].data = bytes(DropedCoverImage[0])
					except:
						pass
					MP3Data.save()
					setCoverMP3.save()
			elif 2 <= len(EditFilePath):
				if not len(EditMediaPath_FLAC) == 0:
					for FlacFilePath in EditMediaPath_FLAC:
						FLACData = mutagen.flac.FLAC(FlacFilePath)
						if not PropertyDiaLog.TrackName.text() == '(複数の値)':
							try:
								FLACData.tags['title'] = PropertyDiaLog.TrackName.text()
							except:
								pass
						if not PropertyDiaLog.TrackArtist.text() == '(複数の値)':
							try:
								FLACData.tags['artist'] = PropertyDiaLog.TrackArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbumArtist.text() == '(複数の値)':
							try:
								FLACData.tags['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbum.text() == '(複数の値)':
							try:
								FLACData.tags['album'] = PropertyDiaLog.TrackAlbum.text()
							except:
								pass
						if not PropertyDiaLog.TrackGenre.text() == '(複数の値)':
							try:
								FLACData.tags['genre'] = PropertyDiaLog.TrackGenre.text()
							except:
								pass
						if not PropertyDiaLog.TrackYear.text() == '(複数の値)':
							try:
								FLACData.tags['date'] = PropertyDiaLog.TrackYear.text()
							except:
								pass
						if not PropertyDiaLog.TrackNum.text() == '(複数の値)':
							try:
								FLACData.tags['tracknumber'] = PropertyDiaLog.TrackNum.text()
							except:
								pass
						if DropedCheck[0] == '1':
							try:
								cover_picture = mutagen.flac.Picture()
								cover_picture.data = bytes(DropedCoverImage[0])
								FLACData.clear_pictures()
								FLACData.add_picture(cover_picture)
							except:
								pass
							pass
						FLACData.save()
				if not len(EditMediaPath_M4A) == 0:
					for M4AFilePath in EditMediaPath_M4A:
						M4AData = mutagen.mp4.MP4(M4AFilePath)
						if not PropertyDiaLog.TrackName.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9nam'] = PropertyDiaLog.TrackName.text()
							except:
								pass
						if not PropertyDiaLog.TrackArtist.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9ART'] = PropertyDiaLog.TrackArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbumArtist.text() == '(複数の値)':
							try:
								M4AData.tags['aART'] = PropertyDiaLog.TrackAlbumArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbum.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9alb'] = PropertyDiaLog.TrackAlbum.text()
							except:
								pass
						if not PropertyDiaLog.TrackGenre.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9gen'] = PropertyDiaLog.TrackGenre.text()
							except:
								pass
						if not PropertyDiaLog.TrackYear.text() == '(複数の値)':
							try:
								M4AData.tags['\xa9day'] = PropertyDiaLog.TrackYear.text()
							except:
								pass
						if not PropertyDiaLog.TrackNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackNum.text() == '':
									M4AData.tags['trkn'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackNum.text():
									if not '/' in PropertyDiaLog.TrackNum.text():
										M4AData.tags['trkn'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
									else:
										M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]), int(PropertyDiaLog.TrackNum.text().split()[1]))]
								else:
									M4AData.tags['trkn'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
							except:
								pass
						if not PropertyDiaLog.TrackDiscNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackDiscNum.text() == '':
									M4AData.tags['disk'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
									if not '/' in PropertyDiaLog.TrackDiscNum.text():
										M4AData.tags['disk'] = [(0, PropertyDiaLog.TrackDiscNum.text())]
									else:
										M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]), int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
								else:
									M4AData.tags['disk'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
							except:
								pass
						if DropedCheck[0] == '1':
							try:
								M4AData.tags['covr'] = [bytes(DropedCoverImage[0])]
							except:
								pass
						M4AData.save()
				if not len(EditMediaPath_MP3) == 0:
					for MP3FilePath in EditMediaPath_MP3:
						MP3Data = EasyID3(MP3FilePath)
						setCoverMP3 = mutagen.id3.ID3(MP3FilePath)
						if not PropertyDiaLog.TrackName.text() == '(複数の値)':
							try:
								MP3Data['title'] = PropertyDiaLog.TrackName.text()
							except:
								pass
						if not PropertyDiaLog.TrackArtist.text() == '(複数の値)':
							try:
								MP3Data['artist'] = PropertyDiaLog.TrackArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbumArtist.text() == '(複数の値)':
							try:
								MP3Data['albumartist'] = PropertyDiaLog.TrackAlbumArtist.text()
							except:
								pass
						if not PropertyDiaLog.TrackAlbum.text()  == '(複数の値)':
							try:
								MP3Data['album'] = PropertyDiaLog.TrackAlbum.text()
							except:
								pass
						if not PropertyDiaLog.TrackGenre.text() == '(複数の値)':
							try:
								MP3Data['genre'] = PropertyDiaLog.TrackGenre.text()
							except:
								pass
						if not PropertyDiaLog.TrackYear.text() == '(複数の値)':
							try:
								MP3Data['data'] = PropertyDiaLog.TrackYear.text()
							except:
								pass
						if not PropertyDiaLog.TrackNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackNum.text() == '':
									MP3Data['tracknumber'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackNum.text():
									if not '/' in PropertyDiaLog.TrackNum.text():
										MP3Data['tracknumber'] = [(0, int(PropertyDiaLog.TrackNum.text()))]
									else:
										MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split('/')[0]), int(PropertyDiaLog.TrackNum.text().split()[1]))]
								else:
									MP3Data['tracknumber'] = [(int(PropertyDiaLog.TrackNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackNum.text().split(' / ')[1]))]
							except:
								pass
						if not PropertyDiaLog.TrackDiscNum.text() == '(複数の値)':
							try:
								if PropertyDiaLog.TrackDiscNum.text() == '':
									MP3Data['discnumber'] = [(0, 0)]
								elif not ' / ' in PropertyDiaLog.TrackDiscNum.text():
									if not '/' in PropertyDiaLog.TrackDiscNum.text():
										MP3Data['discnumber'] = [(0, int(PropertyDiaLog.TrackDiscNum.text()))]
									else:
										MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split('/')[0]), int(PropertyDiaLog.TrackDiscNum.text().split()[1]))]
								else:
									MP3Data['discnumber'] = [(int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[0]), int(PropertyDiaLog.TrackDiscNum.text().split(' / ')[1]))]
							except:
								pass
						if DropedCheck[0] == '1':
							try:
								setCoverMP3['APIC:'].data = bytes(DropedCoverImage[0])
							except:
								pass
						MP3Data.save()
						setCoverMP3.save()
		DropedCheck[0] = '0'
		EditFilePath[0:] = []

	def CopyPath(self):
		QApplication.clipboard().setText(self.ListView.selectedIndexes()[0].data())

	def mouseDoubleClicked(self):
		QDesktopServices.openUrl('file:///{}'.format(self.ListView.selectedIndexes()[0].data()))

	def show(self):
		self.w.exec()

class MainWindowwView(QMainWindow):
	fileDropped = Signal(list)
	def __init__(self, parent=None):
		super(MainWindowwView, self).__init__(parent)
		self.setAcceptDrops(True)
		self.setWindowIcon(QIcon(QPixmap(QSize(512, 512)).fromImage(QImage.fromData(QByteArray.fromBase64(b'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')))))

	def closeEvent(self, event):
		OutOfThread0.exit(0)
		super(MainWindowwView, self).closeEvent(event)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
			for ff in event.mimeData().urls():
				newpath = '{}{}{}'.format(PathListory[0], '/', str(ff.toLocalFile()).split('/')[-1])
				try:
					if os.path.isfile(str(ff.toLocalFile())):
							shutil.move(str(ff.toLocalFile()), newpath)
					else:
						shutil.move(str(ff.toLocalFile()), newpath)
				except:
					pass
		else:
			event.ignore()

	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(Qt.CopyAction)
			event.setAccepted(True)
			event.accept()
			for c in event.mimeData().urls():
				newpath = '{}{}{}'.format(PathListory[0], '/', str(c.toLocalFile()).split('/')[-1])
				try:
					if os.path.isfile(str(c.toLocalFile())):
							shutil.move(str(c.toLocalFile()), newpath)
					else:
						shutil.move(str(c.toLocalFile()), newpath)
				except:
					pass
		else:
			event.ignore()

	def setLocation(self): # 右下に配置
		AvailableWindow = QGuiApplication.primaryScreen().availableGeometry()
		ScreenGeometoryWindow = QGuiApplication.primaryScreen().geometry()
		widget = self.geometry()
		x = AvailableWindow.width() - widget.width()
		y = 2 * AvailableWindow.height() - ScreenGeometoryWindow.height() - widget.height()
		self.move(x, y)

	def setLocation2(self): # 左上に配置
		AvailableWindow = QGuiApplication.primaryScreen().availableGeometry()
		ScreenGeometoryWindow = QGuiApplication.primaryScreen().geometry()
		widget = self.geometry()
		x = AvailableWindow.width() - ScreenGeometoryWindow.width()
		y = 2 * AvailableWindow.height() - ScreenGeometoryWindow.height() - 2 * widget.height()
		self.move(x, y)

class DeletingOKDialog(QDialog):
	def __init__(self):
		super(DeletingOKDialog, self).__init__()
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.setWindowTitle('削除の確認')
		self.setFixedSize(200, 100)
		self.Label1 = QLabel('本当に削除しますか？', self)
		self.Label1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.selectorButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.selectorButton.accepted.connect(self.accept)
		self.selectorButton.rejected.connect(self.reject)
		self.selectorButton.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.Popup = QGridLayout()
		self.Popup.addWidget(self.Label1, 0, 0, Qt.AlignCenter)
		self.Popup.addWidget(self.selectorButton, 1, 0, Qt.AlignCenter)
		self.setLayout(self.Popup)

	@staticmethod
	def OutPutResult():
		d = DeletingOKDialog()
		d.exec()
		if d.result() == QDialog.Accepted:
			return '0'
		elif d.result() == QDialog.Rejected:
			return '1'

class ForceDeletingOKDialog(QDialog):
	def __init__(self):
		super(ForceDeletingOKDialog, self).__init__()
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.setWindowTitle('削除の確認')
		self.setFixedSize(210, 100)
		self.Label1 = QLabel('本当に完全削除しますか？', self)
		self.Label1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.selectorButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.selectorButton.accepted.connect(self.accept)
		self.selectorButton.rejected.connect(self.reject)
		self.selectorButton.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.Popup = QGridLayout()
		self.Popup.addWidget(self.Label1, 0, 0, Qt.AlignCenter)
		self.Popup.addWidget(self.selectorButton, 1, 0, Qt.AlignCenter)
		self.setLayout(self.Popup)

	@staticmethod
	def OutPutResult():
		d = ForceDeletingOKDialog()
		d.exec()
		if d.result() == QDialog.Accepted:
			return '0'
		elif d.result() == QDialog.Rejected:
			return '1'

class NewFileCreateDialog(QDialog):
	def __init__(self):
		super(NewFileCreateDialog, self).__init__()
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.setWindowTitle('新しいファイルの作成')
		self.setFixedSize(300, 100)
		self.Label1 = QLabel('新しいファイルの名前を入れてください', self)
		self.Label1.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.CreateInput1 = QLineEdit()
		self.CreateInput1.setClearButtonEnabled(True)
		self.CreateInput1.setPlaceholderText('ここに新しいファイルの名前を入れてください')
		self.CreateInput1.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
		self.selectorButton1 = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.selectorButton1.accepted.connect(self.accept)
		self.selectorButton1.rejected.connect(self.reject)
		self.selectorButton1.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.Popup = QGridLayout()
		self.Popup.addWidget(self.Label1, 0, 0)
		self.Popup.addWidget(self.CreateInput1, 1, 0)
		self.Popup.addWidget(self.selectorButton1, 2, 0, Qt.AlignCenter)
		self.setLayout(self.Popup)

	def InputResult(self):
		return self.CreateInput1.text()

	@staticmethod
	def OutputResults():
		r = NewFileCreateDialog()
		r.exec()
		input_result = r.InputResult()
		if r.result() == QDialog.Accepted and r.result() != QDialog.Rejected:
			return input_result, '0'
		else:
			return '', '1'

class NewCreateFolderDialog(QDialog):
	def __init__(self):
		super(NewCreateFolderDialog, self).__init__()
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.setWindowTitle('新しいフォルダの作成')
		self.setFixedSize(300, 100)
		self.Label = QLabel('新しい名前を入れてください', self)
		self.Label.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.CreateInput = QLineEdit()
		self.CreateInput.setText('新規フォルダ')
		self.CreateInput.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
		self.CreateInput.setClearButtonEnabled(True)
		self.CreateInput.setPlaceholderText('ここに新しい名前を入れてください')
		self.selectorButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.selectorButton.accepted.connect(self.accept)
		self.selectorButton.rejected.connect(self.reject)
		self.selectorButton.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.Popup = QGridLayout()
		self.Popup.addWidget(self.Label, 0, 0)
		self.Popup.addWidget(self.CreateInput, 1, 0)
		self.Popup.addWidget(self.selectorButton, 2, 0, Qt.AlignCenter)
		self.setLayout(self.Popup)

	def InputResult(self):
		return self.CreateInput.text()

	@staticmethod
	def OutputResult():
		r = NewCreateFolderDialog()
		r.exec()
		input_result = r.InputResult()
		if r.result() == QDialog.Accepted and r.result() != QDialog.Rejected:
			return input_result, '0'
		else:
			return '', '1'

class InputDiaLog(QDialog):
	def __init__(self):
		super(InputDiaLog, self).__init__()
		self.setStyleSheet('QDialog{background-color: #2d2d2d;color: #ededed;}')
		self.setWindowTitle('名前の変更')
		self.setFixedSize(300, 100)
		self.Label = QLabel('新しい名前を入れてください', self)
		self.Label.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;}')
		self.renameInput = QLineEdit()
		self.renameInput.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
		self.renameInput.setText(SelectedItemPath[0])
		self.renameInput.setClearButtonEnabled(True)
		self.renameInput.setPlaceholderText('ここに新しい名前を入れてください')
		self.selectorButton = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		self.selectorButton.accepted.connect(self.accept)
		self.selectorButton.rejected.connect(self.reject)
		self.selectorButton.setStyleSheet('QDialogButtonBox{background-color: #2d2d2d;color: #ededed;} QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.Popup = QGridLayout()
		self.Popup.addWidget(self.Label, 0, 0)
		self.Popup.addWidget(self.renameInput, 1, 0)
		self.Popup.addWidget(self.selectorButton, 2, 0, Qt.AlignCenter)
		self.setLayout(self.Popup)

	def InputResult(self):
		return self.renameInput.text()

	@staticmethod
	def OutputResult():
		r = InputDiaLog()
		r.exec()
		input_result = r.InputResult()
		if r.result() == QDialog.Accepted and r.result() != QDialog.Rejected:
			return input_result, '0'
		else:
			return '', '1'

class Ui_FullTools2(object):
	def setupUi(self, FullTools2):
		if not FullTools2.objectName():
			FullTools2.setObjectName("FullTools2")
		FullTools2.resize(1145, 638)
		FullTools2.setStyleSheet('QWidget{background-color: #292828;color: White;}')
		self.FullTools2 = FullTools2
		self.Tab3 = QTabWidget(FullTools2)
		self.Tab3.setObjectName("Tab3")
		self.Tab3.setGeometry(QRect(0, 10, 1141, 631))
		self.Tab3.setStyleSheet('QWidget{background-color: #2d2d2d;color: #2d2d2d;} QTabBar::tab{background-color: #2d2d2d;color: White;border: 2px solid #1a1a1a;border-color: #1a1a1a;}')
		self.tab = QWidget()
		self.tab.setObjectName("tab")
		self.FileFinput = QLineEdit(self.tab)
		self.FileFinput.setObjectName("FileFinput")
		self.FileFinput.setGeometry(QRect(92, 20, 269, 31))
		self.FileFinput.setPlaceholderText('ここにファイル名を入力してください')
		self.FileFinput.setStyleSheet('QLineEdit#FileFinput{color: White;background-color: #131519;border 0px;}')
		self.FileOption = QCheckBox(self.tab)
		self.FileOption.setObjectName("FileOption")
		self.FileOption.setGeometry(QRect(612, 20, 199, 31))
		self.FileOption.setStyleSheet('QCheckBox#FileOption{color: White;}')
		self.FileTypeOption = QCheckBox(self.tab)
		self.FileTypeOption.setObjectName("FileTypeOption")
		self.FileTypeOption.setGeometry(QRect(392, 20, 219, 31))
		self.FileTypeOption.setStyleSheet('QCheckBox#FileTypeOption{color: White;}')
		self.FileName = QLabel(self.tab)
		self.FileName.setObjectName("FileName")
		self.FileName.setGeometry(QRect(12, 26, 79, 21))
		self.FileName.setStyleSheet('QLabel#FileName{color: White;}')
		self.FileFinput_2 = QLineEdit(self.tab)
		self.FileFinput_2.setObjectName("FileFinput_2")
		self.FileFinput_2.setGeometry(QRect(92, 70, 269, 31))
		self.FileFinput_2.setPlaceholderText('ここに場所を入力します(例: /)')
		self.FileFinput_2.setStyleSheet('QLineEdit#FileFinput_2{color: White;background-color: #131519;border 0px;}')
		self.FileSystemModel = QFileSystemModel()
		self.FileSystemModel.setRootPath(os.path.expanduser("~"))
		self.FileSystemModel.setNameFilters(['*.app'])
		self.FileSystemModel.setNameFilterDisables(False)
		self.FileSearchInput = QLineEdit(self.tab)
		self.FileSearchInput.textChanged.connect(self.on_TextSearch)
		self.FileSearchInput.setObjectName("FileSearchInput")
		self.FileSearchInput.setGeometry(QRect(0, 130, 331, 35))
		self.FileSearchInput.setPlaceholderText('ここにフォルダ名を入力して検索できます')
		self.FileSearchInput.setStyleSheet('QLineEdit#FileSearchInput {background-color: #2d2d2d;color: #ededed;border 0px;}')
		self.FolderTree = QTreeView(self.tab)
		self.FolderTree.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.FolderTree.header().setVisible(False)
		self.FolderTree.setObjectName("FolderTree")
		self.FolderTree.setGeometry(QRect(0, 160, 359, 441))
		self.FolderTree.setModel(self.FileSystemModel)
		try:
			self.FolderTree.setRootIndex(self.FileSystemModel.index(os.path.splitdrive(os.environ['windir'])[0] + '/'))
		except:
			self.FolderTree.setRootIndex(self.FileSystemModel.index('/'))
		self.FolderTree.setStyleSheet('QTreeView#FolderTree{color: White;background-color: #131519;}')
		self.FolderTree.setColumnWidth(0 ,300)
		self.FolderTree.setColumnHidden(1, True)
		self.FolderTree.setColumnHidden(2, True)
		self.FolderTree.setColumnHidden(3, True)
		self.FolderTree.clicked.connect(self.SelectedItem)
		self.FolderName = QLabel(self.tab)
		self.FolderName.setObjectName("FolderName")
		self.FolderName.setGeometry(QRect(12, 74, 79, 21))
		self.FolderName.setStyleSheet('QLabel#FolderName{color: White;}')
		self.label_2 = QLabel(self.tab)
		self.label_2.setObjectName("label_2")
		self.label_2.setGeometry(QRect(1, 110, 341, 21))
		self.label_2.setStyleSheet('QLabel#label_2{color: White;}')
		self.DebugArea = QPlainTextEdit(self.tab)
		self.DebugArea.setObjectName("DebugArea")
		self.DebugArea.setGeometry(QRect(322, 440, 809, 161))
		self.DebugArea.setReadOnly(True)
		self.DebugArea.setStyleSheet('QPlainTextEdit#DebugArea{color: White;background-color: #131519;}')
		self.ResultTree = QTreeView(self.tab)
		self.ResultTree.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ResultTree.setObjectName("ResultTree")
		self.ResultTree.setGeometry(QRect(322, 130, 809, 312))
		self.ResultTree.setAutoScroll(False)
		self.ResultTree.setColumnWidth(0 ,400)
		self.ResultTree.setHeaderHidden(1)
		self.ResultTree.setStyleSheet('QTreeView#ResultTree {color: #e4e4e4;background-color: #131519;outline: 0;font-size: 14px;font-weight: 500;text-transform: capitarise;show-decoration-selected: 1;qproperty-indentation: 24;}')
		self.SearchButton = QPushButton(self.tab)
		self.SearchButton.setObjectName("SearchButton")
		self.SearchButton.setGeometry(QRect(402, 67, 239, 41))
		self.SearchButton.setStyleSheet('QPushButton#SearchButton{background-color: #2d2d2d;color: White;}')
		self.SearchButton.pressed.connect(self.SearchingFile)
		self.ResultDelButton = QPushButton(self.tab)
		self.ResultDelButton.setObjectName("ResultDelButton")
		self.ResultDelButton.setGeometry(QRect(922, 67, 209, 41))
		self.ResultDelButton.pressed.connect(self.ClearDebug)
		self.ResultDelButton.setStyleSheet('QPushButton#ResultDelButton{background-color: #2d2d2d;color: #FF0000;}')
		self.Tab3.addTab(self.tab, "")
		self.tab_2 = QWidget()
		self.tab_2.setObjectName("tab_2")
		self.resultMOdel = QStandardItemModel()
		self.ResultView2Model = QStandardItemModel()
		self.ResultView2 = QTreeView(self.tab_2)
		self.ResultView2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.ResultView2.setObjectName("ResultView2")
		self.ResultView2.setHeaderHidden(1)
		self.ResultView2.setGeometry(QRect(433, 131, 703, 321))
		self.ResultView2.setStyleSheet('QTreeView#ResultView2{color: White;background-color: #131519;}')
		self.FolderPath = QLineEdit(self.tab_2)
		self.FolderPath.setObjectName("FolderPath")
		self.FolderPath.setGeometry(QRect(140, 60, 335, 31))
		self.FolderPath.setStyleSheet('QLineEdit#FolderPath{color: White;background-color: #131519;border 0px;}')
		self.FolderPath.setPlaceholderText('ここに検索したい場所を入力してください')
		self.FolderPathLabel = QLabel(self.tab_2)
		self.FolderPathLabel.setObjectName("FolderPathLabel")
		self.FolderPathLabel.setGeometry(QRect(5, 67, 122, 20))
		self.FolderPathLabel.setStyleSheet('QLabel#FolderPathLabel{color: White;}')
		font = QFont()
		font.setPointSize(13)
		self.FolderPathLabel.setFont(font)
		self.BigFileSearchButton = QPushButton(self.tab_2)
		self.BigFileSearchButton.setObjectName("BigFileSearchButton")
		self.BigFileSearchButton.setGeometry(QRect(492, 54, 239, 41))
		self.BigFileSearchButton.pressed.connect(self.BigFileSearching)
		self.BigFileSearchButton.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.FileSystemModel2 = QFileSystemModel()
		self.FileSystemModel2.setRootPath(os.path.expanduser("~"))
		self.FileSystemModel2.setNameFilters(['*.app'])
		self.FileSystemModel2.setNameFilterDisables(False)
		self.InputView2 = QTreeView(self.tab_2)
		self.InputView2.setObjectName("InputView2")
		self.InputView2.setGeometry(QRect(1, 170, 440, 431))
		self.InputView2.setModel(self.FileSystemModel2)
		self.InputView2.clicked.connect(self.SelectedItem2)
		try:
			self.InputView2.setRootIndex(self.FileSystemModel2.index(os.path.splitdrive(os.environ['windir'])[0] + '/'))
		except:
			self.InputView2.setRootIndex(self.FileSystemModel2.index('/'))
		self.InputView2.setStyleSheet('QTreeView{color: White;background-color: #131519;}')
		self.InputView2.header().setVisible(False)
		self.InputView2.setColumnWidth(0, 300)
		self.InputView2.setColumnHidden(1, True)
		self.InputView2.setColumnHidden(2, True)
		self.InputView2.setColumnHidden(3, True)
		self.InputView2.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.DebugLog2 = QPlainTextEdit(self.tab_2)
		self.DebugLog2.setObjectName("DebugLog2")
		self.DebugLog2.setGeometry(QRect(440, 451, 696, 151))
		self.DebugLog2.setReadOnly(True)
		self.DebugLog2.setStyleSheet('QPlainTextEdit{color: White;background-color: #131519;}')
		self.ResultDelButton2 = QPushButton(self.tab_2)
		self.ResultDelButton2.setObjectName("ResultDelButton2")
		self.ResultDelButton2.setGeometry(QRect(922, 70, 209, 41))
		self.ResultDelButton2.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.ResultDelButton2.pressed.connect(self.ClearDebug2)
		self.Tab3.addTab(self.tab_2, "")
		self.tab_3 = QWidget()
		self.tab_3.setObjectName("tab_3")
		self.SearchInputer = QLineEdit(self.tab_2)
		self.SearchInputer.setObjectName("SearchInputer")
		self.SearchInputer.textChanged.connect(self.on_TextSearch2)
		self.SearchInputer.setGeometry(QRect(1, 130, 442, 42))
		self.SearchInputer.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;}')
		self.SearchInputer.setPlaceholderText('ここに検索したいフォルダを入力してください')
		self.FolderSearchLabel2 = QLabel(self.tab_2)
		self.FolderSearchLabel2.setObjectName("FolderSearchLabel2")
		self.FolderSearchLabel2.setGeometry(QRect(12, 110, 439, 21))
		self.FolderSearchLabel2.setStyleSheet("QLabel#FolderSearchLabel2{\n"
"color: White;\n"
"}")
		self.DiskScrollArea = QScrollArea(self.tab_3)
		self.DiskScrollArea.setStyleSheet('QScrollArea QAbstractScrollArea{background-color: #1a1a1a;alternate-background-color: #1a1a1a;color: #1a1a1a;} QScrollArea{background-color: #292828;color: #ededed;}')
		self.DiskScrollArea.setGeometry(QRect(620, 210, 535, 395))
		self.DiskScrollArea.setWidget(DiskPieWidget())
		self.DiskScrollArea.verticalScrollBar().setDisabled(True)
		self.SystemInfoWidget = SystemInfoWidget(self.tab_3)
		self.SystemInfoWidget.setGeometry(QRect(10, 10, 266, 588))
		self.VevrticalFrame = QLabel(self.tab_3)
		self.VevrticalFrame.setAlignment(Qt.AlignCenter)
		self.VevrticalFrame.setStyleSheet('QLabel{background-color: #2d2d2d;color: #ededed;border:1px solid #ededed;}')
		self.VevrticalFrame.setGeometry(QRect(590, 0, 1, 605))
		self.VevrticalFrame.setMaximumWidth(1)
		self.Clock = pyqtgraph.GraphicsLayoutWidget(self.tab_3, show=True)
		self.Clock.resize(190, 190)
		self.Clock.move(940, 10)
		self.Clock.setBackground(background=(45, 45, 45))
		self.Clock.setRange(QRect(0, 0, 800, 800))
		self.Clock.setContentsMargins(0, 0, 0, 0)
		self.ClockMain = self.Clock.addPlot()
		self.ClockMain.setMenuEnabled(False)
		self.ClockMain.showAxis('bottom', False)
		self.ClockMain.showAxis('left', False)
		self.ClockMain.setAspectLocked(lock=True)
		self.ClockMain.setMouseEnabled(x=False, y=False)
		self.XClockShaft = 1 * numpy.cos(numpy.linspace(0, 2 * numpy.pi, 1000))
		self.YClockShaft = 1 * numpy.sin(numpy.linspace(0, 2 * numpy.pi, 1000))
		self.ClockMain.plot(self.XClockShaft, self.YClockShaft, pen=pyqtgraph.mkPen(width=2, color=(182, 202, 147)))
		for sec in range(60):
			self.line_length = 0.1 if sec % 5 == 0 else 0.03
			self.line_width = 4 if sec % 5 == 0 else 1.5
			self.X1Memory = numpy.sin(numpy.radians(360 * (sec / 60))) * 1
			self.X2Memory = numpy.sin(numpy.radians(360 * (sec / 60))) * (1 - self.line_length)
			self.Y1Memory = numpy.cos(numpy.radians(360 * (sec / 60))) * 1
			self.Y2Memory = numpy.cos(numpy.radians(360 * (sec / 60))) * (1 - self.line_length)
			self.ClockPen = pyqtgraph.mkPen(width=self.line_width, color=(182, 202, 147))
			self.ClockPen.setCapStyle(Qt.RoundCap)
			self.ClockMain.plot([self.X1Memory, self.X2Memory], [self.Y1Memory, self.Y2Memory], pen=self.ClockPen)
		self.HourTexts = []
		for Hour in range(1, 13, 1):
			self.XShaft = numpy.sin(numpy.radians(360 * (Hour / 12))) * 1 * 0.8
			self.YShaft = numpy.cos(numpy.radians(360 * (Hour / 12))) * 1 * 0.8
			self.ClockHourText = pyqtgraph.TextItem(text=str(Hour), anchor=(0.5, 0.5), color=(182, 202, 147))
			self.ClockHourText.setPos(self.XShaft, self.YShaft)
			self.ClockFont = QFont()
			self.ClockFont.setPixelSize(70)
			self.ClockHourText.setFont(self.ClockFont)
			self.ClockMain.addItem(self.ClockHourText)
			self.HourTexts.append(self.ClockHourText)
		self.ClockShortTimeHandPen = pyqtgraph.mkPen(width=9, color=(162, 193, 105))
		self.ClockShortTimeHandPen.setCapStyle(Qt.RoundCap)
		self.ClockShortTimeHand = self.ClockMain.plot(pen=self.ClockShortTimeHandPen)
		self.ClockLongTimeHandPen = pyqtgraph.mkPen(width=5, color=(205, 238, 147))
		self.ClockLongTimeHandPen.setCapStyle(Qt.RoundCap)
		self.ClockLongTimeHand = self.ClockMain.plot(pen=self.ClockLongTimeHandPen)
		self.ClockSecTimehandPen = pyqtgraph.mkPen(width=2, color=(233, 88, 88))
		self.ClockSecTimehandPen.setCapStyle(Qt.RoundCap)
		self.ClockSecTimehand = self.ClockMain.plot(pen=self.ClockSecTimehandPen)
		self.ClockUpdateTime = QTimer()
		self.ClockUpdateTime.timeout.connect(self.ClockTimeSet)
		self.ClockUpdateTime.start(50)
		self.Calender = QCalendarWidget(self.tab_3)
		self.Calender.setObjectName('Calender')
		self.Calender.setStyleSheet('QCalendarWidget QTableView{background-color: #1a1a1a;alternate-background-color: #1a1a1a;color: #ededed;} QCalendarWidget QAbstractItemView{selection-background-color: #2d2d2d;alternate-background-color: #1a1a1a;selection-color: #ededed;} QCalendarWidget QMenu{background-color: #1a1a1a;color: #ededed;} QCalendarWidget QToolButton{background-color: #1a1a1a;color: #ededed;} QCalendarWidget QWidget{background-color: #1a1a1a;alternate-background-color: #1a1a1a;color: #ededed;} QCalendarWidget QWidget{background-color: #1a1a1a;alternate-background-color: #1a1a1a;color: #ededed;}')
		self.Calender.setGridVisible(True)
		self.Calender.setDateEditEnabled(False)
		self.Calender.clicked.connect(None)
		self.Calender.setGeometry(QRect(630, 15, 270, 175))
		self.Calender.setLocale(QLocale(QLocale.Japanese, QLocale.Japan))
		self.Calender.setSelectionMode(QCalendarWidget.NoSelection)
		self.CalenderFont = QFont()
		self.CalenderFont.setPointSize(8)
		self.Calender.setFont(self.CalenderFont)
		self.Tab3.addTab(self.tab_2, "")
		self.Tab3.addTab(self.tab_3, "")
		self.Tab3.addTab(self.tab_3, "")
		self.tab_4 = QWidget()
		self.tab_4.setObjectName("tab_4")
		self.RootFolderFileSystemModel = QFileSystemModel()
		self.RootFolderFileSystemModel.setReadOnly(False)
		self.RootFolderFileSystemModel.setRootPath(os.path.expanduser("~"))
		self.RootFolderTree = QTreeView(self.tab_4)
		self.RootFolderTree.setDragEnabled(True)
		self.RootFolderTree.setDragDropOverwriteMode(True)
		self.RootFolderTree.setDragDropMode(QAbstractItemView.DragDrop)
		self.RootFolderTree.setDefaultDropAction(Qt.MoveAction)
		self.RootFolderTree.setObjectName("RootFolderTree")
		self.RootFolderTree.setGeometry(QRect(0, 80, 279, 541))
		self.RootFolderTree.setModel(self.RootFolderFileSystemModel)
		self.RootFolderTree.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.RootFolderTree.setStyleSheet('QTreeView{color: White;background-color: #131519;border 0px;}')
		try:
			self.RootFolderTree.setRootIndex(self.RootFolderFileSystemModel.index(os.path.splitdrive(os.environ['windir'])[0] + '/'))
		except:
			self.RootFolderTree.setRootIndex(self.RootFolderFileSystemModel.index('/'))
		self.RootFolderTree.setHeaderHidden(True)
		self.RootFolderTree.setColumnWidth(0, 200)
		self.RootFolderTree.setColumnHidden(1, True)
		self.RootFolderTree.setColumnHidden(2, True)
		self.RootFolderTree.setColumnHidden(3, True)
		self.RootFolderTree.setIconSize(QSize(30, 30))
		self.RootFolderTree.doubleClicked.connect(self.SelectedFolder)
		self.RootFolderTree.clicked.connect(self.SingleClickRootFolder)
		self.RootFolderTree.setContextMenuPolicy(Qt.CustomContextMenu)
		self.RootFolderTree.customContextMenuRequested.connect(self.FilerContextMenu)
		self.SubFolderTree = FileSystemListView(self.tab_4)
		self.SubFolderTree.setObjectName("SubFolderTree")
		self.SubFolderTree.setDragEnabled(True)
		self.SubFolderTree.setDragDropOverwriteMode(True)
		self.SubFolderTree.setDragDropMode(QAbstractItemView.DragDrop)
		self.SubFolderTree.setDefaultDropAction(Qt.MoveAction)
		self.SubFolderTree.doubleClicked.connect(self.AccessFolder)
		self.SubFolderTree.clicked.connect(self.SinglePreviewSubFolder)
		self.SubFolderTree.setStyleSheet('QListView{color: White;background-color: #131519;border 0px;}')
		self.PathBar = QLineEdit(self.tab_4)
		self.PathBar.setObjectName("PathBar")
		self.PathBar.setGeometry(QRect(143, 38, 618, 41))
		self.PathBar.editingFinished.connect(self.EndEditSearchBar)
		self.PathBar.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;border 0px;}')
		self.FileTreeSearch2 = QLineEdit(self.tab_4)
		self.FileTreeSearch2.setObjectName("FileTreeSearch2")
		self.FileTreeSearch2.editingFinished.connect(self.on_TextSearch5)
		self.FileTreeSearch2.setClearButtonEnabled(True)
		self.FileTreeSearch2.setGeometry(QRect(802, 36, 335, 41))
		self.FileTreeSearch2.setStyleSheet('QLineEdit{background-color: #2d2d2d;color: #ededed;border 0px;border 0px;}')
		self.FileTreeSearch2.setPlaceholderText('検索')
		self.UpDirectory = QPushButton(self.tab_4)
		self.UpDirectory.setObjectName("UpDirectory")
		self.UpDirectory.setGeometry(QRect(760, 36, 42, 43))
		self.UpDirectory.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;border 0px;}')
		font2 = QFont()
		font2.setPointSize(24)
		self.UpDirectory.setFont(font2)
		self.UpDirectory.pressed.connect(self.MoveUpDiercory)
		self.PreviewBackground = QPlainTextEdit(self.tab_4)
		self.PreviewBackground.setObjectName("PreviewBackground")
		self.PreviewBackground.setGeometry(QRect(802, 80, 358, 541))
		self.PreviewBackground.setFont(font)
		self.PreviewBackground.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
		self.PreviewBackground.setStyleSheet('QPlainTextEdit{color: White;background-color: #131519;}')
		self.PreviewBackground.setReadOnly(True)
		self.Preview = QLabel(self.tab_4)
		self.Preview.setObjectName("Preview")
		self.Preview.setGeometry(QRect(804, 170, 328, 320))
		self.Preview.setTextFormat(Qt.PlainText)
		self.Preview.setAlignment(Qt.AlignCenter)
		self.Preview.setStyleSheet('QLabel{color: White;background-color: #131519;}')
		self.SortChangeButton = QPushButton(self.tab_4)
		self.SortChangeButton.setObjectName("SortChangeButton")
		self.SortChangeButton.setGeometry(QRect(1032, 12, 109, 21))
		self.SortChangeButton.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.HomeButton = QPushButton(self.tab_4)
		self.HomeButton.setObjectName("HomeButton")
		self.HomeButton.setGeometry(QRect(99, 36, 43, 43))
		self.HomeButton.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.HomeButton.setAutoDefault(False)
		self.HomeButton.pressed.connect(self.BackHome)
		self.BackButton = QPushButton(self.tab_4)
		self.BackButton.setObjectName("BackButton")
		self.BackButton.setGeometry(QRect(10, 36, 43, 43))
		font4 = QFont()
		font4.setPointSize(35)
		self.BackButton.setFont(font4)
		self.BackButton.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.BackButton.pressed.connect(self.BackReturnDirectory)
		self.OnButton = QPushButton(self.tab_4)
		self.OnButton.setObjectName("OnButton")
		self.OnButton.setGeometry(QRect(58, 36, 43, 43))
		self.OnButton.setFont(font4)
		self.OnButton.setStyleSheet('QPushButton{background-color: #2d2d2d;color: #ededed;}')
		self.OnButton.pressed.connect(self.OnMoveDirectory)
		self.SortChangeButton.setText('昇順(A-Z)')
		SortedNumbar[0] = '0'
		self.SortChangeButton.pressed.connect(self.ItemSorting) #1
		self.Tab3.addTab(self.tab_4, "")
		self.FileFolderSelector()
		self.retranslateUi(FullTools2)
		self.Tab3.setCurrentIndex(3)
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()
		self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
		PathHistorys.append(self.SubFolderTree.rootPath()+'/')
		OutOfThread0.start()
		QMetaObject.connectSlotsByName(FullTools2)

	def IconSet(self, type):
		if type == 'home':
			return QIcon(QPixmap(QSize(32, 32)).fromImage(QImage.fromData(QByteArray.fromBase64(b'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aycaxW//9DjW/A9lvfVPtopds1Dx4w/evm58/P59NY41ZyjWTviEYsyaLsWP8wXFL/eZOEPz75up1Grjfqr47X8kjjUnKNb21RRrxx2j+MePjmPNkYp//H2Kfzy+GbP2HsU7/W2coe2Y4xQ/j2MUv3x8JoffiQMVa9f+TvGPf1DxPw9TrO3fVvG/c0MAAQQQQCAHgXqD5Bu22xX/81bFuc43Kv73+xXn+k5W/ASvV/z9P1b8z4Gb+0Ec1/luJYr64psx4/5T8cv9VPFvhW6I4/quV/zjkeIf/6HiH78mjus7UvGPP69E0dB2LnGKM/+uODe+R3Fu9ZWKX+ocxY9zWhxnvqism+f42YpvQC+OMzR/8zXFr/eVOK7XKP4Wn2Lt3IT/rfhxTlL8ch+Js279o4yPcxPvVKJo1f2Kb7x3jTO0nOuK4yZ1Kev2y5yo+HGPjuP++q+KMZs/q6xbzm0dx7llcdyU+OZc/f2hMfX3h1H08vWKMdHWinPbHaz4z1vi95v+uEb8fjOK6u9Hjam/Hx10iiL/jsrf/JFwbggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIVFfg/wO3VQfRarJYKgAAAABJRU5ErkJggg=='))))
		if type == 'back':
			return QIcon(QPixmap(QSize(32, 32)).fromImage(QImage.fromData(QByteArray.fromBase64(b'iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0EAYAAACbRgPJAAAAAXNSR0IArs4c6QAAAMJlWElmTU0AKgAAAAgABgESAAMAAAABAAEAAAEaAAUAAAABAAAAVgEbAAUAAAABAAAAXgEoAAMAAAABAAIAAAExAAIAAAARAAAAZodpAAQAAAABAAAAeAAAAAAAAABIAAAAAQAAAEgAAAABUGl4ZWxtYXRvciAyLjcuMwAAAASQBAACAAAAFAAAAK6gAQADAAAAAQABAACgAgAEAAAAAQAAAfSgAwAEAAAAAQAAAfQAAAAAMjAyMjowODoxMCAxOTozMToxMQA9b/6jAAAACXBIWXMAAAsTAAALEwEAmpwYAAADrmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx0aWZmOllSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpZUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WFJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOlhSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPlBpeGVsbWF0b3IgMi43LjM8L3htcDpDcmVhdG9yVG9vbD4KICAgICAgICAgPHhtcDpDcmVhdGVEYXRlPjIwMjItMDgtMTBUMTk6MzE6MTErMDk6MDA8L3htcDpDcmVhdGVEYXRlPgogICAgICAgICA8eG1wOk1ldGFkYXRhRGF0ZT4yMDIyLTA4LTMxVDE2OjA0OjAyKzA5OjAwPC94bXA6TWV0YWRhdGFEYXRlPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+NTAwPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjUwMDwvZXhpZjpQaXhlbFlEaW1lbnNpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgrcfCqmAABAAElEQVR4AezdCXxU1aHH8XMmIewQwo7si+w7sgkoyC47BLu3r4u1vqf2dV+0i631tc/urbW7tvZVTYCAiqIoIogLoIICAgoisicQVoEkc9/5z+RmMGEJySSZ5Te/z6chc+/ce+73pjKXk5kxhhsCCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACCCCAAAIIIIAAAggggAACSSlgk/KoOWgEEEAAAQQQiGmBvTeqevXqHFVNm5p1qlGjwA9U7doFk5W1KaHb2bP25+rYsYL+Ki+veaY6edKGbp4X0wfL4BBAAAEEECgW4AKdHwUEEEAAAQQQqDYBL3QLBPY2Uk2a1Dum2rUzf1Dt25sNqn1770bVpo3XTbVoYUM1bmweV7Vre48od/W9XJ05Y65Ux4/bPergweB2tXt3yj711lu1NqpNm+qNVgcOhC/cg8FqO3B2hAACCCCAQDkEuEAvBxKrIIAAAggggMDlCYQvxK09lKVatky5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QAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAIFYF/j/AAKch0YLnAQAAAABJRU5ErkJggg=='))))
		if type == 'on':
			return QIcon(QPixmap(QSize(32, 32)).fromImage(QImage.fromData(QByteArray.fromBase64(b'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AAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEAAAQQQQAABBBBAAAEEEEhsgf8PtgvhFk6g7SEAAAAASUVORK5CYII='))))
		if type == 'up':
			return QIcon(QPixmap(QSize(32, 32)).fromImage(QImage.fromData(QByteArray.fromBase64(b'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5dprFx0Z8drzETUdToAAAQIVETCgV6RRyiRAgACB8QosOD+SXaldFLnxxvGezeozCnwjyXLffemJkQsumH6vgBkf7xsECBAgQKBGAgb0GjXTVggQIEBgeIEXHRVZu7Z9feTss9P9I9nHsPkqRCB9V+TJJ5MLI+efv/R/RX7840JO7iQECBAgQKAkAgb0kjRCGQQIECBQDoHFvxe5/vp0S+S886ZfC12O6mpYxZVJlqeeSnZEPvvZ5KzI5z9fw53aEgECBAgQmFUgnfURHkCAAAECBBoo8NjVkUWL2g9FzjgjXR/54Ad7vx/Ze+8GkuS75Q8kWbZubX0j8rnPdftfH//4si0Rdy7ki201AgQIEKiKgAG9Kp1SJwECBAhMRKDX/1q8eMORkfe+N/lF5Hd+p/fDyKGHTqSoCp80PTXyyCPpY5Errui9MnLhhXt+JfLAAxXemtIJECBAgMDIAgb0kQktQIAAAQJNELi3F5ma2uO0yLvelb42cvLJ3d+NvO1tSSeyeHETLOa1xwuSLNu3p7dGbrghvSXyta+1ro18+ct7HB9Zv35ea3owAQIECBCoqYABvaaNtS0CBAgQGK/A+v8RefWrk1si73hH78nIiSe2booceWT3rsiv/dp4qyjf6ukPI9nA/VeR1atb10dWruz+KHLddUv7X6tWDd6d3cfZla+DKiJAgACBSQoY0Cep79wECBAgUHmBwS3w7famL0SOOKJ7RuSoo9ILI698Ze/ayEEHpV+N7LNP94nI0qXpn0cWLkxOiLTbZYfo3dhPL704sm1belxk06buKyKPP55cHFmzJnlH5K67utsiq1fv9cXID384GMi3bi37PtVHgAABAgQmKbBgkid3bgIECBAgUHWBweDZ6Qz2cdtt0/9dtziyeHHn3shBB7VPj+yzT3trZMmSHUdEpqbSP42Uf0BvnRzpdnvHRLZt64TMuNwAAAB/SURBVO0f2by5d0tk7dqF34ysWTP9cXU7+3pVEvFFgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBagn8f6RPFF7K6hbDAAAAAElFTkSuQmCC'))))

	def ClockTimeSet(self):
		degrationSec = (datetime.datetime.now().second / 60) * 360
		degrationMin = (datetime.datetime.now().minute / 60) * 360 + (1 /60) * 360 * (datetime.datetime.now().second / 60)
		degrationHour = (datetime.datetime.now().hour / 12) * 360 + (1 / 12) * 360 * (datetime.datetime.now().minute / 60)
		XShaftOfSec = numpy.sin(numpy.radians(degrationSec)) * 1 * 0.855
		YShaftOfSec = numpy.cos(numpy.radians(degrationSec)) * 1 * 0.855
		self.ClockSecTimehand.setData([0, XShaftOfSec], [0, YShaftOfSec])
		XShaftOfMin = numpy.sin(numpy.radians(degrationMin)) * 1 * 0.82
		YShaftOfMin = numpy.cos(numpy.radians(degrationMin)) * 1 * 0.82
		self.ClockLongTimeHand.setData([0, XShaftOfMin], [0, YShaftOfMin])
		XShaftOfHour = numpy.sin(numpy.radians(degrationHour)) * 1 * 0.55
		YShaftOfHour = numpy.cos(numpy.radians(degrationHour)) * 1 * 0.55
		self.ClockShortTimeHand.setData([0, XShaftOfHour], [0, YShaftOfHour])

	"""def WiFiSpeedRate(self):
		try:
			while True:
				Net_IN1 = psutil.net_io_counters().bytes_recv
				Net_OUT1 = psutil.net_io_counters().bytes_sent
				time.sleep(0.8)
				Net_IN2 = psutil.net_io_counters().bytes_recv
				Net_OUT2 = psutil.net_io_counters().bytes_sent
				NETIN = '{}GB'.format(round((Net_IN2 - Net_IN1) / 1073741824, 1))
				if NETIN[0:2] == '0.':
					NETIN = '{}MB'.format(round((Net_IN2 - Net_IN1) / 1048576, 1))
					if NETIN[0:2] == '0.':
						NETIN = '{}KB'.format(round((Net_IN2 - Net_IN1) / 1024, 1))
						if NETIN[0:2] == '0.':
							NETIN = '{}B'.format((Net_IN2 - Net_IN1))
				NETOUT = '{}GB'.format(round((Net_OUT2 - Net_OUT1) / 1073741824, 1))
				if NETOUT[0:2] == '0.':
					NETOUT = '{}MB'.format(round((Net_OUT2 - Net_OUT1) / 1048576, 1))
					if NETOUT[0:2] == '0.':
						NETOUT = '{}KB'.format(round((Net_OUT2 - Net_OUT1) / 1024, 1))
						if NETOUT[0:2] == '0.':
							NETOUT = '{}B'.format((Net_OUT2 - Net_OUT1))
				self.network.setText('↓{} /s ↑{} /s'.format(NETIN, NETOUT))
		except:
			pass

	def CPUMontor(self):
		try:
			while True:
				self.cpu.setText('{}%'.format(psutil.cpu_percent(interval=0.8)))
		except:
			pass

	def MemoryMonitor(self):
		try:
			while True:
				self.memoryUsedCapacityPercent.setText('{}%'.format(psutil.virtual_memory().percent))
				time.sleep(0.8)
		except:
			pass

	def UsedMemory(self):
		try:
			while True:
				useMemory = '{}GB'.format(round(psutil.virtual_memory().used / 1073741824, 1))
				if useMemory[0:2] == '0.':
					useMemory = '{}MB'.format(round(psutil.virtual_memory().used / 1048576, 1))
					if useMemory[0:2] == '0.':
						useMemory = '{}KB'.format(round(psutil.virtual_memory().used / 1024, 1))
						if useMemory[0:2] == '0.':
							useMemory = '{}B'.format(psutil.virtual_memory().used)
				self.memoryUsed.setText('使用容量: {} / {}GB'.format(useMemory, round(psutil.virtual_memory().total / 1073741824, 1)))
				time.sleep(0.8)
		except:
			pass

	def SubMemoryMonitor(self):
		try:
			while True:
				MemoryFree = '{}GB'.format(round(psutil.virtual_memory().available / 1073741824, 1))
				if MemoryFree[0:2] == '0.':
					MemoryFree = '{}MB'.format(round(psutil.virtual_memory().available / 1048576, 1))
					if MemoryFree[0:2] == '0.':
						MemoryFree = '{}KB'.format(round(psutil.virtual_memory().available / 1024, 1))
						if MemoryFree[0:2] == '0.':
							MemoryFree = '{}B'.format(psutil.virtual_memory().available)
				self.memoryFree.setText('空き容量: {} / {}GB'.format(MemoryFree, round(psutil.virtual_memory().total / 1073741824, 1)))
				time.sleep(0.8)
		except:
			pass

	def SwapMemoryUsedPercent(self):
		try:
			while True:
				self.virtualMemoryUsedCapacity.setText('{}%'.format(psutil.swap_memory().percent))
				time.sleep(0.8)
		except:
			pass

	def SwapUsed(self):
		try:
			while True:
				Swpused = '{}GB'.format(round(psutil.swap_memory().used / 1073741824, 1))
				if Swpused[0:2] == '0.':
					Swpused = '{}MB'.format(round(psutil.swap_memory().used / 1048576, 1))
					if Swpused[0:2] == '0.':
						Swpused = '{}KB'.format(round(psutil.swap_memory().used / 1024, 1))
						if Swpused[0:2] == '0.':
							Swpused = '{}B'.format(psutil.swap_memory().used)
				self.virtualMemoryUsed.setText('使用容量: {} / {}GB'.format(Swpused, round(psutil.swap_memory().total / 1073741824, 1)))
				time.sleep(0.8)
		except:
			pass

	def SwapFree(self):
		try:
			while True:
				SwpFree = '{}GB'.format(round(psutil.swap_memory().free / 1073741824, 1))
				if SwpFree[0:2] == '0.':
					SwpFree = '{}MB'.format(round(psutil.swap_memory().free / 1048576, 1))
					if SwpFree[0:2] == '0.':
						SwpFree = '{}KB'.format(round(psutil.swap_memory().free / 1024, 1))
						if SwpFree[0:2] == '0.':
							SwpFree = '{}B'.format(psutil.swap_memory().free)
				self.virtualMemoryFree.setText('空き容量: {} / {}GB'.format(SwpFree, round(psutil.swap_memory().total / 1073741824, 1)))
				time.sleep(0.8)
		except:
			pass

	def DiskUsedPercent(self):
		try:
			if not os.path.splitdrive(os.environ['windir'])[0] == '':
				mountPath = os.path.splitdrive(os.environ['windir'])[0] + '/'
			else:
				mountPath = '/'
		except KeyError:
			mountPath = '/'
		try:
			while True:
				self.diskUsedCapacity.setText('{}%'.format(psutil.disk_usage(mountPath).percent))
				time.sleep(0.8)
		except:
			pass

	def DiskUsed(self):
		try:
			if not os.path.splitdrive(os.environ['windir'])[0] == '':
				mountPath = os.path.splitdrive(os.environ['windir'])[0] + '/'
			else:
				mountPath = '/'
		except KeyError:
			mountPath = '/'
		try:
			TotalDisk = '{}TB'.format(round(psutil.disk_usage(mountPath).total / 1099511627776, 1))
			if TotalDisk[0:2] == '0.':
				TotalDisk = '{}GB'.format(round(psutil.disk_usage(mountPath).total / 1073741824, 1))
				if TotalDisk[0:2] == '0.':
					TotalDisk = '{}MB'.format(round(psutil.disk_usage(mountPath).total / 1048576, 1))
					if TotalDisk[0:2] == '0.':
						TotalDisk = '{}KB'.format(round(psutil.disk_usage(mountPath).total / 1024, 1))
						if TotalDisk[0:2] == '0.':
							TotalDisk = '{}B'.format(psutil.disk_usage(mountPath).total)
			while True:
				diskUseBytes = '{}TB'.format(round(psutil.disk_usage(mountPath).used / 1099511627776, 1))
				if diskUseBytes[0:2] == '0.':
					diskUseBytes = '{}GB'.format(round(psutil.disk_usage(mountPath).used / 1073741824, 1))
					if diskUseBytes[0:2] == '0.':
						diskUseBytes = '{}MB'.format(round(psutil.disk_usage(mountPath).used / 1048576, 1))
						if diskUseBytes[0:2] == '0.':
							diskUseBytes = '{}KB'.format(round(psutil.disk_usage(mountPath).used / 1024, 1))
							if diskUseBytes[0:2] == '0.':
								diskUseBytes = '{}B'.format(psutil.disk_usage(mountPath).used)
				self.diskUsed.setText('使用容量: {} / {}'.format(diskUseBytes, TotalDisk))
				time.sleep(0.8)
		except:
			pass

	def DiskFree(self):
		try:
			if not os.path.splitdrive(os.environ['windir'])[0] == '':
				mountPath = os.path.splitdrive(os.environ['windir'])[0] + '/'
			else:
				mountPath = '/'
		except KeyError:
			mountPath = '/'
		try:
			TotalDisk = '{}TB'.format(round(psutil.disk_usage(mountPath).total / 1099511627776, 1))
			if TotalDisk[0:2] == '0.':
				TotalDisk = '{}GB'.format(round(psutil.disk_usage(mountPath).total / 1073741824, 1))
				if TotalDisk[0:2] == '0.':
					TotalDisk = '{}MB'.format(round(psutil.disk_usage(mountPath).total / 1048576, 1))
					if TotalDisk[0:2] == '0.':
						TotalDisk = '{}KB'.format(round(psutil.disk_usage(mountPath).total / 1024, 1))
						if TotalDisk[0:2] == '0.':
							TotalDisk = '{}B'.format(psutil.disk_usage(mountPath).total)
			while True:
				diskFreeBytes = '{}TB'.format(round(psutil.disk_usage(mountPath).free / 1099511627776, 1))
				if diskFreeBytes[0:2] == '0.':
					diskFreeBytes = '{}GB'.format(round(psutil.disk_usage(mountPath).free / 1073741824, 1))
					if diskFreeBytes[0:2] == '0.':
						diskFreeBytes = '{}MB'.format(round(psutil.disk_usage(mountPath).free / 1048576, 1))
						if diskFreeBytes[0:2] == '0.':
							diskFreeBytes = '{}KB'.format(round(psutil.disk_usage(mountPath).free / 1024, 1))
							if diskFreeBytes[0:2] == '0.':
								diskFreeBytes = '{}KB'.format(psutil.disk_usage(mountPath).free)
				self.diskFree.setText('空き容量: {} / {}'.format(diskFreeBytes, TotalDisk))
				time.sleep(0.8)
		except:
			pass"""

	def OnMoveDirectory(self):
		for path in reversed(PathHistorys):
			if not self.SubFolderTree.rootPath() == path and StopPath2[0] == '0':
				self.SubFolderTree.setRootPath(path)
				self.SubFolderTree.setRootIndex(self.SubFolderTree.index(path))
				self.PathBar.setText(path)
				StopPath2[0] = '1'
				break
		BackupRootPath.append(self.SubFolderTree.rootPath())
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()

	def BackReturnDirectory(self):
		try:
			BackPath = self.SubFolderTree.rootPath().split([p for p in self.SubFolderTree.rootPath().split('/')][-1])[0]
		except:
			BackPath = ''
		if BackPath == '':
			try:
				BackPath = os.path.splitdrive(os.environ['windir'.lower()])[0]
			except:
				try:
					BackPath = os.path.splitdrive(os.environ['windir'.upper()])[0]
				except:
					BackPath = '/'
		if PathHistorys[0] == BackPath:
			StopPath[0] = '1'
			self.SubFolderTree.setRootPath(BackPath)
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(BackPath))
			self.PathBar.setText(BackPath)
			PathHistorys.append(self.SubFolderTree.rootPath())
			StopPath2[0] = '0'
		elif not PathHistorys[0] == BackPath and StopPath[0] == '0':
			if PathHistorys[0] == self.SubFolderTree.rootPath()+'/' and StopPath[0] == '0':
				pass
			else:
				self.SubFolderTree.setRootPath(BackPath)
				self.SubFolderTree.setRootIndex(self.SubFolderTree.index(BackPath))
				self.PathBar.setText(BackPath)
				PathHistorys.append(self.SubFolderTree.rootPath())
				StopPath2[0] = '0'
		elif StopPath[0] == '1' and PathHistorys[0] == self.SubFolderTree.rootPath()+'/':
			BackPath = os.path.expanduser('~')+'/'
			self.SubFolderTree.setRootPath(BackPath)
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(BackPath))
			self.PathBar.setText(BackPath)
			PathHistorys.append(self.SubFolderTree.rootPath())
			StopPath2[0] = '0'
		elif StopPath[0] == '0' and not str(pathlib.Path(os.path.expanduser('~')).parent) == self.SubFolderTree:
			BackPath = PathHistorys[-2]
			self.SubFolderTree.setRootPath(BackPath)
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(BackPath))
			self.PathBar.setText(BackPath)
			PathHistorys.append(self.SubFolderTree.rootPath())
			StopPath2[0] = '0'
		elif StopPath[0] == '2':
			BackPath = PathHistorys[-2]
			self.SubFolderTree.setRootPath(BackPath)
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(BackPath))
			self.PathBar.setText(BackPath)
			PathHistorys.append(self.SubFolderTree.rootPath())
			StopPath[0] = '0'
			StopPath2[0] = '0'
		BackupRootPath.append(self.SubFolderTree.rootPath())
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()

	def BackHome(self):
		self.SubFolderTree.setRootPath(os.path.expanduser('~'))
		self.SubFolderTree.setRootIndex(self.SubFolderTree.index(os.path.expanduser('~')))
		self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()
		PathHistorys.append(self.SubFolderTree.rootPath()+'/')
		StopPath[0] = '0'
		StopPath2[0] = '0'
		BackupRootPath.append(self.SubFolderTree.rootPath())
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()

	def MoveUpDiercory(self):
		try:
			DriveLatter = os.path.splitdrive(os.environ['windir'.lower()])[0]
		except:
			try:
				DriveLatter = os.path.splitdrive(os.environ['windir'.upper()])[0]
			except:
				DriveLatter = '/'

		self.SubFolderTree.setRootPath(os.path.dirname(self.SubFolderTree.rootPath()))
		self.SubFolderTree.setRootIndex(self.SubFolderTree.index(self.SubFolderTree.rootPath()))
		if not self.SubFolderTree.rootPath() == DriveLatter:
			self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
		else:
			self.PathBar.setText(self.SubFolderTree.rootPath())
		PathHistorys.append(self.SubFolderTree.rootPath()+'/')
		StopPath[0] = '0'
		StopPath2[0] = '0'
		BackupRootPath.append(self.SubFolderTree.rootPath())
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()

	def AccessFolder(self):
		if not os.path.isfile(self.SubFolderTree.filePath(self.SubFolderTree.selectedIndexes()[0])):
			self.SubFolderTree.setRootPath(self.SubFolderTree.filePath(self.SubFolderTree.selectedIndexes()[0]))
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(self.SubFolderTree.filePath(self.SubFolderTree.selectedIndexes()[0])))
			self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
			StopPath[0] = '0'
			StopPath2[0] = '0'
			PathHistorys.append(self.SubFolderTree.rootPath()+'/')
			NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()
			BackupRootPath.append(self.SubFolderTree.rootPath())
		else:
			QDesktopServices.openUrl('file:///{}'.format(self.SubFolderTree.filePath(self.SubFolderTree.selectedIndexes()[0])))
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()

	def EndEditSearchBar(self):
		if self.PathBar.text() == '../':
			self.SubFolderTree.setRootPath(os.path.dirname(self.SubFolderTree.rootPath()+'/'))
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(self.SubFolderTree.rootPath()+'/'))
			self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
			PathHistorys.append(self.SubFolderTree.rootPath()+'/')
			StopPath[0] = '0'
			StopPath2[0] = '0'
			BackupRootPath.append(self.SubFolderTree.rootPath())
		elif self.PathBar.text() == '.':
			self.SubFolderTree.setRootPath(self.SubFolderTree.rootPath()+'/')
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(self.SubFolderTree.rootPath()+'/'))
			self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
			StopPath[0] = '0'
			StopPath2[0] = '0'
			PathHistorys.append(self.SubFolderTree.rootPath()+'/')
			BackupRootPath.append(self.SubFolderTree.rootPath())
		else:
			self.SubFolderTree.setRootPath(self.PathBar.text())
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(self.SubFolderTree.rootPath()+'/'))
			self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
			StopPath[0] = '0'
			StopPath2[0] = '0'
			PathHistorys.append(self.SubFolderTree.rootPath()+'/')
			BackupRootPath.append(self.SubFolderTree.rootPath())
		NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()

	def SingleClickRootFolder(self):
		try:
			RootIndex = self.RootFolderTree.selectedIndexes()[0]
		except:
			RootIndex = self.RootFolderTree.selectedIndexes()
		if self.RootFolderTree.isExpanded(RootIndex):
			self.RootFolderTree.collapse(RootIndex)
		else:
			self.RootFolderTree.expand(RootIndex)

	def SinglePreviewSubFolder(self):
		SelectedItem[0] = self.SubFolderTree.selectedIndexes()
		PixelMap = QPixmap(self.SubFolderTree.filePath(self.SubFolderTree.selectedIndexes()[0]))
		if PixelMap.isNull():
			self.Preview.setText('プレビューできませんでした')
		else:
			self.Preview.setPixmap(PixelMap.scaled(self.Preview.width(), self.Preview.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

	def FilerContextMenu(self, Point):
		self.Menu1 = QMenu()
		self.Menu1.setStyleSheet('QMenu{background-color: #2d2d2d;color: #ededed;} QMenu::item:selected{background-color: #af0c00;color: #ededed;}')
		try:
			if os.path.isfile(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0])):
				self.Menu1.addAction('開く', self.OpenFile)
				self.Menu1.addAction('コピー', self.CopyFile)
				self.Menu1.addAction('削除', self.Deleting)
			else:
				self.Menu1.addAction('コピー', self.CopyFile)
				self.Menu1.addAction('フォルダの新規作成', self.CreateFolder)
				self.Menu1.addAction('フォルダを開く', self.OpenFile)
				self.Menu1.addAction('ここにコピー', self.CopyiedFiles)
			self.Menu1.exec(self.RootFolderTree.mapToGlobal(Point))
		except:
			pass

	def OpenFile(self):
		QDesktopServices.openUrl('file:///{}'.format(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0])))

	def CopyFile(self):
		CopiedItems[0] = [self.RootFolderFileSystemModel.filePath(countItem) for countItem in self.RootFolderTree.selectedIndexes()]
		CopiedItemCount[0] = len(self.RootFolderTree.selectedIndexes())

	def CreateFolder(self):
		Result = NewCreateFolderDialog.OutputResult()
		if Result[1] == '0':
			if not Result[0] == '':
				if not Result[0] == ' ':
					try:
						os.mkdir('{}{}{}'.format(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0]), '/', Result[0]))
					except:
						for c in range(9999):
							try:
								os.mkdir('{}{}{} ({})'.format(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0]), '/', Result[0], c))
								break
							except:
								pass

	def CopyiedFiles(self):
		try:
			if not self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0]) == '':
				self.RootPath = self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0])
			else:
				self.RootPath = os.path.expanduser('~')
		except:
			self.RootPath = os.path.expanduser('~')
		if CopiedItemCount[0] == len(CopiedItems[0]):
			for CopiedItem in CopiedItems[0]:
				newPath = '{}{}{}'.format(self.RootPath, '/', CopiedItem.split('/')[-1])
				if not QFile.exists(newPath):
					QFile.copy(CopiedItem, newPath)
				else:
					for cc in range(9999):
						if not QFile.exists('{} ({}).{}'.format(newPath.split('.')[0], cc+1, newPath.split('.')[-1])):
							QFile.copy(CopiedItem, '{} ({}).{}'.format(newPath.split('.')[0], cc+1, newPath.split('.')[-1]))
							break
						else:
							pass

	def Deleting(self):
		if os.path.isfile(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0])):
			send2trash.send2trash(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0]))
		else:
			send2trash.send2trash(self.RootFolderFileSystemModel.filePath(self.RootFolderTree.selectedIndexes()[0]))

	def ItemSorting(self):
		if SortedNumbar[0] == '1':
			self.SortChangeButton.setText('昇順(A-Z)')
			self.SubFolderTree.sort(0, Qt.SortOrder.AscendingOrder)
			SortedNumbar[0] = '0'
		elif SortedNumbar[0] == '0':
			self.SortChangeButton.setText('降順(Z-A)')
			self.SubFolderTree.sort(0, Qt.SortOrder.DescendingOrder)
			SortedNumbar[0] = '1'

	def SortingItemMenu(self):
		if SortedNumbar[0] == '1':
			self.SortChangeButton.setText('昇順(A-Z)')
			self.SubFolderTree.sort(0, Qt.SortOrder.AscendingOrder)
			SortedNumbar[0] = '0'
		elif SortedNumbar[0] == '0':
			self.SortChangeButton.setText('降順(Z-A)')
			self.SubFolderTree.sort(0, Qt.SortOrder.DescendingOrder)
			SortedNumbar[0] = '1'

	def on_TextSearch(self, text):
		try:
			if not self.FolderTree.isExpanded(self.FolderTree.selectedIndexes()[0]):
				self.FolderTree.expandRecursively(self.FolderTree.selectedIndexes()[0], 3)
		except:
			pass
		self.FolderTree.keyboardSearch('')
		self.FolderTree.keyboardSearch(text)

	def on_TextSearch2(self, text):
		try:
			if not self.InputView2.isExpanded(self.InputView2.selectedIndexes()[0]):
				self.InputView2.expandRecursively(self.InputView2.selectedIndexes()[0], 3)
		except:
			pass
		self.InputView2.keyboardSearch('')
		self.InputView2.keyboardSearch(text)

	def on_TextSearch4(self, text):
		try:
			if not self.RootFolderTree.isExpanded(self.RootFolderTree.selectedIndexes()[0]):
				self.RootFolderTree.expandRecursively(self.RootFolderTree.selectedIndexes()[0], 3)
		except:
			pass
		self.RootFolderTree.keyboardSearch('')
		self.RootFolderTree.keyboardSearch(text)

	def from_item_to_json(self, parent, data):
		for c in range(len(data)):
			path = json.loads(data[c]).get('PATH')
			if os.path.isfile(path):
				AcceptFileType = ('.svg', '.jpg', '.jpeg', '.png', '.bmp', '.gif', '.rgb', '.tiff', '.xbm', '.pbm', '.pgm', '.ppm')
				try:
					if path.lower().endswith(AcceptFileType):
						icon = QIcon(LoadThread.submit(self.LoadImage, path).result())
					if path.lower().endswith('.flac'):
						icon = QIcon(self.LoadFLAC(path))
					if path.lower().endswith('.m4a'):
						icon = QIcon(self.LoadM4A(path))
					if path.lower().endswith('.mp3'):
						icon = QIcon(self.LoadMP3(path))
					if not path.lower().endswith(('.flac', '.m4a', '.mp3')) and not path.lower().endswith(AcceptFileType):
						icon = QFileIconProvider().icon(QFileIconProvider.File)
				except:
					icon = QFileIconProvider().icon(QFileIconProvider.File)
			else:
				icon = QFileIconProvider().icon(QFileIconProvider.Folder)
			c2 = QStandardItem(icon, path)
			parent.appendRow(c2)

	def LoadImage(self, path):
		try:
			img = QPixmap(QSize(32, 32))
			img.load(path)
			return img
		except:
			pass

	def LoadFLAC(self, path):
		return QPixmap(QSize(64, 64)).fromImage(QImage.fromData(mutagen.flac.FLAC(path).pictures[0].data))

	def LoadMP3(self, path):
		return QPixmap(QSize(64, 64)).fromImage(QImage.fromData(mutagen.mp3.MP3(path)['APIC:'].data))

	def LoadM4A(self, path):
		return QPixmap(QSize(64, 64)).fromImage(QImage.fromData(mutagen.mp4.MP4(path)['covr'][0]))

	def on_TextSearch5(self):
		if not self.FileTreeSearch2.text() == '':
			DicFiles = []
			for File in pathlib.Path(self.SubFolderTree.rootPath()+'/').glob('**/{}'.format(self.FileTreeSearch2.text())):
				DicFiles.append(json.dumps({'PATH': '{}'.format(str(File))}, indent=2, ensure_ascii=False))
			self.ItemModel = QStandardItemModel()
			self.from_item_to_json(self.ItemModel.invisibleRootItem(), sorted(DicFiles))
			SearchWindow(model=self.ItemModel).show()

	def SelectedItem(self, index):
		try:
			rootIndex = self.FolderTree.selectedIndexes()[0]
			self.FolderTree.expand(rootIndex)
		except:
			pass
		if os.path.isfile(self.FileSystemModel.filePath(self.FileSystemModel.index(index.row(), 0, index.parent()))):
			pass
		else:
			self.FileFinput_2.setText(self.FileSystemModel.filePath(self.FileSystemModel.index(index.row(), 0, index.parent())))

	def SelectedItem2(self, index):
		try:
			rootIndex2 = self.InputView2.selectedIndexes()[0]
			self.InputView2.expand(rootIndex2)
		except:
			pass
		if os.path.isfile(self.FileSystemModel2.filePath(self.FileSystemModel2.index(index.row(), 0, index.parent()))):
			pass
		else:
			self.FolderPath.setText(self.FileSystemModel2.filePath(self.FileSystemModel2.index(index.row(), 0, index.parent())))

	def SelectedFolder(self):
		try:
			RootIndex = self.RootFolderTree.selectedIndexes()[0]
		except:
			RootIndex = self.RootFolderTree.selectedIndexes()
		if not os.path.isfile(self.RootFolderFileSystemModel.filePath(RootIndex)):
			if self.RootFolderTree.isExpanded(RootIndex):
				self.RootFolderTree.collapse(RootIndex)
			else:
				self.RootFolderTree.expand(RootIndex)
			PathListory[0] = self.RootFolderFileSystemModel.filePath(RootIndex)
			self.SubFolderTree.setRootPath(self.RootFolderFileSystemModel.filePath(RootIndex))
			self.SubFolderTree.setRootIndex(self.SubFolderTree.index(self.RootFolderFileSystemModel.filePath(RootIndex)))
			self.PathBar.setText(self.SubFolderTree.rootPath()+'/')
			NowRootDirectoryPath[0] = self.SubFolderTree.rootPath()
			StopPath[0] = '2'
			StopPath2[0] = '0'
			PathHistorys.append(self.SubFolderTree.rootPath()+'/')
			BackupRootPath.append(self.SubFolderTree.rootPath())
		else:
			QDesktopServices.openUrl('file:///{}'.format(self.RootFolderFileSystemModel.filePath(RootIndex)))

	def FileFolderSelector(self):
		if self.FileFinput.text() == '**':
			self.FileFinput.setText('*.*')
		self.FileOption.stateChanged.connect(self.FileFolderSelectorCallBak)
		self.FileTypeOption.stateChanged.connect(self.FileFolderSelectorCallBak)
		if self.FileFinput.text() == '**':
			self.FileFinput.setText('*.*')

	def FileFolderSelectorCallBak(self):
		if self.FileTypeOption.checkState() == Qt.Checked:
			if not '*' in self.FileFinput.text():
				try:
					FileName = self.FileFinput.text().split('.')[0]
				except:
					FileName = ''
				try:
					FileType = self.FileFinput.text().split('.')[1]
				except:
					FileType = ''
				if FileName == '':
					FileName = ''
				if FileType == '':
					FileType = '.*'
				if FileName == '' and FileType == '':
					FileName = ''
					FileType = '.*'
				if not '**' in self.FileFinput.text():
					self.FileFinput.setText('{}{}'.format(FileName, FileType).replace('..', '.'))
				else:
					self.FileFinput.setText('*.*')
			elif self.FileOption.checkState() == Qt.Checked and self.FileTypeOption.checkState() == Qt.Checked:
				self.FileFinput.setText('*.*')
			elif self.FileFinput.text() == '*.*':
				self.FileFinput.setText('*.')
			elif self.FileFinput.text() == '*.':
				self.FileFinput.setText('.*')
			elif '*' in self.FileFinput.text() and self.FileOption.checkState() == Qt.Checked:
				if '.' in self.FileFinput.text() and not '*' in self.FileFinput.text():
					try:
						Fname = self.FileFinput.text().split('.')[0]
					except:
						Fname = ''
					try:
						Ftype = self.FileFinput.text().split('.')[1]
					except:
						Ftype = ''
					self.FileFinput.setText('{}{}'.format(Fname, Ftype))
				elif self.FileFinput.text() == '*.':
					self.FileFinput.setText('.*')
				else:
					self.FileFinput.setText('*.*')
		elif self.FileOption.checkState() == Qt.Unchecked and self.FileTypeOption.checkState() == Qt.Unchecked:
			self.FileFinput.setText(self.FileFinput.text().replace('.*', '').replace('*.', '').replace('*', ''))
		if self.FileOption.checkState() == Qt.Checked:
			self.dPrint('[INFO] ファイル名を設定しました。ファイル名: {}'.format(self.FileFinput.text().split('.')[0]))
		if self.FileOption.checkState() == Qt.Checked:
			if not '*' in self.FileFinput.text():
				try:
					FileName = self.FileFinput.text().split('.')[0]
				except:
					FileName = ''
				try:
					FileType = self.FileFinput.text().split('.')[1]
				except:
					FileType = ''
				if FileName == '':
					FileName = '*.'
				if FileType == '':
					FileType = ''
				if FileName == '' and FileType == '':
					FileName = '*.'
					FileType = ''
				if not '**' in self.FileFinput.text():
					self.FileFinput.setText('{}{}'.format(FileName, FileType).replace('..', '.'))
				else:
					self.FileFinput.setText('*.*')
			elif self.FileOption.checkState() == Qt.Checked and self.FileTypeOption.checkState() == Qt.Checked:
				self.FileFinput.setText('*.*')
			elif self.FileFinput.text() == '*.*':
				self.FileFinput.setText('.*')
			elif self.FileFinput.text() == '.*':
				self.FileFinput.setText('*.')
			elif '*' in self.FileFinput.text() and self.FileTypeOption.checkState() == Qt.Checked:
				if '.' in self.FileFinput.text() and not '*' in self.FileFinput.text():
					try:
						Fname = self.FileFinput.text().split('.')[0]
					except:
						Fname = ''
					try:
						Ftype = self.FileFinput.text().split('.')[1]
					except:
						Ftype = ''
					self.FileFinput.setText('{}{}'.format(Fname, Ftype))
				else:
					self.FileFinput.setText('*.*')
		elif self.FileOption.checkState() == Qt.Unchecked and self.FileTypeOption.checkState() == Qt.Unchecked:
			self.FileFinput.setText(self.FileFinput.text().replace('.*', '').replace('*.', '').replace('*', ''))
		if self.FileTypeOption.checkState() == Qt.Checked:
			self.dPrint('[INFO] ファイルタイプを設定しました。ファイルタイプ: {}'.format(self.FileFinput.text().split('.')[1]))

	def dPrint(self, Log):
		self.DebugArea.appendPlainText(Log)

	def dPrint2(self, Logs):
		self.DebugLog2.appendPlainText(Logs)

	def Fill_Model_from_Json(self, Partent, data, path=''):
		if isinstance(data, dict):
			for itm, childs in data.items():
				if itm == '／':
					Icon = QFileIconProvider().icon(QFileIconProvider.Drive)
				elif os.path.isdir(path) or not os.path.isfile(path):
					Icon = QFileIconProvider().icon(QFileIconProvider.Folder)
				else:
					Icon = QFileIconProvider().icon(QFileIconProvider.File)
				child = QStandardItem(Icon, str(itm))
				Partent.appendRow(child)
				self.Fill_Model_from_Json(child, childs)

		elif isinstance(data, list):
			for P in data:
				self.Fill_Model_from_Json(Partent, P)
		else:
			Partent.appendRow(QStandardItem(str(data)))

	def FindAllFiles(self, path):
		for root, dirC, file in os.walk(path):
			yield root
			for File in file:
				yield os.path.join(root, File)

	def BigFileSearching(self):
		DicsFiles = []
		FoundFiles = []
		size_min_mb = 50 << 20
		for File in self.FindAllFiles(self.FolderPath.text()):
			try:
				if os.path.isfile(File):
					if os.path.getsize(File) >= size_min_mb:
						if os.path.getsize(File) >> 20:
							FoundFiles.append(File)
						self.dPrint2('[INFO] ファイルが見つかりました! 使用容量: {:.1f}MB 場所: {}'.format(os.path.getsize(File) >> 20, File))
			except:
				pass
		try:
			DriveLetter = os.path.splitdrive(os.environ['windir'])[0] + '/'
		except:
			DriveLetter = '／'
		for Dics in FoundFiles:
			DicsLists = Dics.split('/')
			PathDics = ''.join(pathlist.replace(pathlist, '{"'+pathlist+'": ') for pathlist in DicsLists)
			SearcedPathDic = re.sub('($)', '}'*(len(DicsLists)), PathDics).replace('{"": ', '{"%s": ' % DriveLetter).replace(': }', ': {}}')
			EndValue = re.findall('(".+": )', json.dumps(ast.literal_eval(SearcedPathDic), indent=2, ensure_ascii=False))[-1].split(':')[0]
			PathJson = json.dumps(ast.literal_eval(SearcedPathDic), ensure_ascii=False).replace('{' + EndValue + ': {}', EndValue).replace('}','') + '}' * (len(DicsLists) - 1)
			DicsFiles.append([PathJson, Dics])
		for DicsF, Path in DicsFiles:
			try:
				self.Fill_Model_from_Json(self.ResultView2Model.invisibleRootItem(), ast.literal_eval(DicsF), Path)
			except:
				continue
		self.ResultView2.setModel(self.ResultView2Model)
		self.ResultView2.expandAll()

	def SearchingFile(self):
		FileAppends = []
		DicFiles = []

		for File in pathlib.Path(self.FileFinput_2.text()).glob('**/{}'.format(self.FileFinput.text())):
			self.dPrint('[INFO] ファイルが見つかりました! 場所: {}'.format(File))
			FileAppends.append(str(File))

		try:
			DriveLetter = os.path.splitdrive(os.environ['windir'])[0] + '/'
		except:
			DriveLetter = '／'
		for dics in FileAppends:
			DicsList = dics.split('/')
			PDic = ''.join(pathlist.replace(pathlist, '{"'+pathlist+'": ') for pathlist in DicsList)
			PathDic = re.sub('($)', '}'*(len(DicsList)), PDic).replace('{"": ', '{"%s": ' % DriveLetter).replace(': }', ': {}}')
			EndValue = re.findall('(".+": )', json.dumps(ast.literal_eval(PathDic), indent=2, ensure_ascii=False))[-1].split(':')[0]
			PathJson = json.dumps(ast.literal_eval(PathDic), ensure_ascii=False).replace('{' + EndValue + ': {}', EndValue).replace('}', '') + '}' * (len(DicsList) -1)
			DicFiles.append([PathJson, dics])
		for DicsFF, Path in DicFiles:
				self.Fill_Model_from_Json(self.resultMOdel.invisibleRootItem(), ast.literal_eval(DicsFF), path=Path)
		self.ResultTree.setModel(self.resultMOdel)
		self.ResultTree.expandAll()


	def ClearDebug(self):
		self.DebugArea.clear()
		self.resultMOdel.removeRows(0, self.resultMOdel.rowCount())

	def ClearDebug2(self):
		self.DebugLog2.clear()
		self.ResultView2Model.removeRows(0, self.ResultView2Model.rowCount())

	def retranslateUi(self, Extend):
		Extend.setWindowTitle(QCoreApplication.translate("Searcher", "ExtendExplorerTools", None))
		self.FileOption.setText(QCoreApplication.translate("Searcher", "ファイル名を無指定", None))
		self.FileTypeOption.setText(QCoreApplication.translate("Searcher", "ファイル拡張子を無指定", None))
		self.FileName.setText(QCoreApplication.translate("Searcher", "ファイル名:", None))
		self.FolderName.setText(QCoreApplication.translate("Searcher", "フォルダ名:", None))
		self.label_2.setText(QCoreApplication.translate("Searcher", "以下からもフォルダを選択できます", None))
		self.SearchButton.setText(QCoreApplication.translate("Searcher", "ファイル検索を開始", None))
		self.ResultDelButton.setText(QCoreApplication.translate("Searcher", "結果を消す", None))
		self.Tab3.setTabText(self.Tab3.indexOf(self.tab), QCoreApplication.translate("Searcher", "ファイルの詳細検索", None))
		self.FolderPathLabel.setText(QCoreApplication.translate("Searcher", "検索したい場所:", None))
		self.BigFileSearchButton.setText(QCoreApplication.translate("Searcher", "ファイル検索を開始", None))
		self.ResultDelButton2.setText(QCoreApplication.translate("Searcher", "結果を消す", None))
		self.Tab3.setTabText(self.Tab3.indexOf(self.tab_2), QCoreApplication.translate("Searcher", "大きいファイルの詳細検索", None))
		self.Tab3.setTabText(self.Tab3.indexOf(self.tab_3), QCoreApplication.translate("Searcher", "システムの情報", None))
		self.FolderSearchLabel2.setText(QCoreApplication.translate("FullTools2", "以下からもフォルダを選択できます", None))
		self.Tab3.setTabText(self.Tab3.indexOf(self.tab_4), QCoreApplication.translate("FullTools2", "エクスプローラー", None))
		self.UpDirectory.setIcon(self.IconSet('up'))
		self.UpDirectory.setToolTip(QCoreApplication.translate("FullTools2", "<html><head/><body><p>上の階層に戻る</p></body></html>", None))
		self.HomeButton.setIcon(self.IconSet('home'))
		self.BackButton.setIcon(self.IconSet('back'))
		self.OnButton.setIcon(self.IconSet('on'))

def main():
	app = QApplication(sys.argv)
	main_window = MainWindowwView()
	ui_window = Ui_FullTools2()
	ui_window.setupUi(main_window)
	main_window.setFixedSize(main_window.size())
	main_window.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()
