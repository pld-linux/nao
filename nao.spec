Summary:	nao - powerful and flexible file manager
Summary(pl):	nao - pot�ny i elastyczny zarz�dca plik�w
Name:		nao
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://nao.linux.pl/data/%{name}-%{version}.tar.bz2
# Source0-md5:	55cb4f2447e0ccfa37ba0ad13eb74c03
URL:		http://nao.linux.pl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fox-devel >= 1.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libpng-devel
BuildRequires:	libssh-devel
Requires:	fox >= 1.4.0
Obsoletes:	openspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nao is powerful, flexible, and utterly configurable file manager
for UNIX systems, written using the FOX toolkit. Main features of
nao are:

 - Support for two panel view and single panel view.
 - Graphically configurable.
 - Powerful file recognition system allows you to configure how files
   of different types are shown (with colors and icons), and what happens
   when you doubleclick them.
 - Long operations are run in separated thread like for example
   copying/moving - you can use program during this process.
 - Extensibility - two types of plugins - you can download and install
   them easily from configuration menu in program.
 - Virtual File System plugins adds supports for file systems like ftp,
   compressed files (tar.bz2,tar.gz) - you can use them like local files.
 - Drag and Drop support compatible with KDE and GNOME applications.

%description -l pl
nao jest pot�nym, elastycznym oraz ca�kowicie konfigurowalnym
zarz�dc� plik�w dla system�w uniksowych, napisanym przy u�yciu
biblioteki FOX. G��wne jego cechy to:

 - Obs�uga zar�wno dwupanelowego jak i jednopanelowego trybu pracy.
 - Graficzna konfiguracja.
 - Pot�ny system rozpoznawania plik�w pozwala na konfiguracj� sposobu
   przedstawiania r�nych typ�w plik�w (kolory, ikony), oraz akcji im
   przypisanej.
 - Czasoch�onne operacje, takie jak przenoszenie czy kopiowanie, s�
   uruchamiane w oddzielnym w�tku, co pozwala na korzystanie z zarz�dcy
   podczas tych czynno�ci.
 - Rozszerzalno�� - dwa typy wtyczek - mo�na je �atwo instalowa�
   korzystaj�c z menu konfiguracyjnego.
 - Wtyczka dla wirtualnego systemu plik�w. Mo�na u�ywa� FTP oraz
   archiw�w jak lokalnych plik�w.
 - Obs�uga "przeci�gnij i upu��" kompatybilna z aplikacjami KDE i
   GNOME.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nao.conf
%{_sysconfdir}/mimeapp
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
