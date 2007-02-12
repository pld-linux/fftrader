Summary:	Final Frontier Trader - space strategy game
Summary(pl.UTF-8):	Final Frontier Trader - strategia kosmiczna
Name:		fftrader
Version:	0.65
Release:	0.1
License:	GPL
Group:		X11/Games
Source0:	http://dl.sourceforge.net/fftrader/%{name}-src-%{version}.zip
# Source0-md5:	062945a80e47d9e0f62a209c22c4f45d
#Patch0:		%{name}-makefile.patch
Patch1:		%{name}-path.patch
URL:		http://fftrader.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	physfs-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Final Frontier Trader is a 2D single player space strategy game. You
pilot a startship which is upgradable. You can buy, sell, or trade
parts and even new startships. You can even join a fleet for
experience in mission and combat.
 
%description -l pl.UTF-8
Final Frontier Trader jest jednoosobową strategią kosmiczną 2D. Gracz
pilotuje statkiem kosmicznym, który jest unowocześniany. Może kupić,
sprzedać lub handlować częściami statku lub nim całym. Może nawet
dołączyć do floty w celu zdobycia doświadczenia w misji i w walce.

%prep
%setup -q -c -T
unzip -qq -a %{SOURCE0}
#%patch0 -p1
%patch1 -p1

%build
rm -f *.dll
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#%%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install fft $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/fpk
install fonts/arial.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}
install fpk/*fpk $RPM_BUILD_ROOT%{_datadir}/%{name}/fpk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO TODO.txt CHANGELOG CHANGELOG.txt README README.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/arial.ttf
%dir %{_datadir}/%{name}/fpk
%{_datadir}/%{name}/fpk/*.fpk
