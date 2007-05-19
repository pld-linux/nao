#
# Conditional build:
%bcond_with	python		# python plugins (unknown requires)
%bcond_without	ssh		# sftp virtual file system
%bcond_without	ssl		# ftp over ssl support
#
Summary:	nao - powerful and flexible file manager
Summary(pl.UTF-8):	nao - potężny i elastyczny zarządca plików
Name:		nao
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://nao.linux.pl/data/%{name}-%{version}.tar.bz2
# Source0-md5:	b113c79af37fae2f6a7b12496900952e
Patch0:		%{name}-desktop.patch
URL:		http://nao.linux.pl/
BuildRequires:	boost-any-devel
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-mem_fn-devel
BuildRequires:	boost-program_options-devel
%{?with_python:BuildRequires:	boost-python-devel}
BuildRequires:	boost-ref-devel
BuildRequires:	boost-regex-devel
BuildRequires:	boost-thread-devel
BuildRequires:	fox-devel >= 1.4.0
BuildRequires:	libpng-devel
%{?with_ssh:BuildRequires:  	libssh-devel}
BuildRequires:	libtool
BuildRequires:	libxml2-devel
%{?with_ssl:BuildRequires:  	openssl-devel}
Requires:	fox >= 1.4.0
Obsoletes:	openspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed

%description
nao is powerful, flexible, and utterly configurable file manager for
UNIX systems, written using the FOX toolkit. Main features of nao are:

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

%description -l pl.UTF-8
nao jest potężnym, elastycznym oraz całkowicie konfigurowalnym
zarządcą plików dla systemów uniksowych, napisanym przy użyciu
biblioteki FOX. Główne jego cechy to:

 - Obsługa zarówno dwupanelowego jak i jednopanelowego trybu pracy.
 - Graficzna konfiguracja.
 - Potężny system rozpoznawania plików pozwala na konfigurację
   sposobu przedstawiania różnych typów plików (kolory, ikony), oraz
   akcji im przypisanej.
 - Czasochłonne operacje, takie jak przenoszenie czy kopiowanie, są
   uruchamiane w oddzielnym wątku, co pozwala na korzystanie z zarządcy
   podczas tych czynności.
 - Rozszerzalność - dwa typy wtyczek - można je łatwo instalować
   korzystając z menu konfiguracyjnego.
 - Wtyczka dla wirtualnego systemu plików. Można używać FTP oraz
   archiwów jak lokalnych plików.
 - Obsługa "przeciągnij i upuść" kompatybilna z aplikacjami KDE i
   GNOME.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{?with_ssh:--enable-sshvfs} \
	%{?with_ssh:--enable-ssl} \
	%{?with_python:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nao.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mime2program.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
