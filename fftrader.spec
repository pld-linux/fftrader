Summary:	-
Summary(pl):	-
Name:		fftrader
Version:	0.65
Release:	0.1
License:	GPL
Group:		X11/Games
Source0:	http://dl.sourceforge.net/fftrader/%{name}-src-%{version}.zip
# Source0-md5:	062945a80e47d9e0f62a209c22c4f45d
#Patch0:		%{name}-what.patch
URL:		-
BuildRequires:	unzip
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -c -T -n %{name}-%{version}
unzip -a %{SOURCE0} > /dev/null
#%patch0 -p1

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
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
