%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define libname %mklibname SonicDENightLight
%define devname %mklibname SonicDENightLight -d

Summary: Library for scheduling the dark-light cycle
Name: sonic-night-light
Version: 6.6.5
Release: %{?git:0.%{git}.}1
URL: https://github.com/Sonic-DE/sonic-night-light
License: GPL
Group: System/Libraries
Source0:  %url/archive/%version/%name-%version.tar.gz

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6Tools)
BuildRequires:	cmake(Qt6ToolsTools)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
# pending rename
# BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:  %{_lib}SonicFrameworksCoreAddons-devel

BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6Test)

Conflicts:      knighttime

%description
Library for scheduling the dark-light cycle

%package -n %libname
Summary: Library for %name
Requires: %name = %{EVRD}
Conflicts: %{_lib}KNightTime

%description -n %libname
%summary

%package -n %devname
Summary: Development files for %name
Requires: %libname = %{EVRD}
Conflicts: %{_lib}KNightTime-devel

%description -n %devname
%summary

%install -a
rm -rf %{buildroot}/%{_libdir}/cmake

%files
%{_libdir}/libexec/knighttimed
%{_datadir}/applications/org.kde.knighttimed.desktop
%{_datadir}/dbus-1/interfaces/org.kde.NightTime.xml
%{_datadir}/dbus-1/services/org.kde.NightTime.service
%{_datadir}/qlogging-categories6/knighttime.categories
%{_userunitdir}/plasma-knighttimed.service

%files -n %libname
%{_libdir}/libKNightTime.*


%files -n %devname
# pending rename
# %{_libdir}/cmake/KNightTime/*.cmake

%{_includedir}/KNightTime/*
